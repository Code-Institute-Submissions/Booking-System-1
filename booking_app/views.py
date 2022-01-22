from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.dateparse import parse_date
from .forms import BookingForm, NewUserForm
from .models import Booking

# Create your views here.


def booking_app(request):
    """ A view to return to the home page """
    return render(request, "booking_app/index.html")


def booking_view(request):
    """ A view to display the booking page and form """
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BookingForm(request.POST)
            date_str = request.POST.get("date")
            form_date = parse_date(date_str)
            book_date = Booking.objects.filter(date=form_date)
            time_str = request.POST.get("time")
            book_time = Booking.objects.filter(time=time_str)
            today = str(date.today())
            if date_str >= today:
                if time_str != "Select a time":
                    if book_time and book_date:
                        form = BookingForm()
                        context = {"form": form}
                        messages.error(
                            request,
                            "This time slot is taken,"
                            " please choose another time.",
                        )
                        return render(
                            request,
                            "booking_app/booking.html",
                            context
                        )
                else:
                    form = BookingForm()
                    context = {"form": form}
                    messages.error(request, "Please Select a time!.")
                    return render(request, "booking_app/booking.html", context)
            else:
                form = BookingForm()
                context = {"form": form}
                messages.error(
                    request,
                    "Please Select a present or future date."
                )
                return render(request, "booking_app/booking.html", context)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
            messages.success(request, "Booking successful.")
            return redirect("my_bookings")
        form = BookingForm()
        context = {"form": form}
        return render(request, "booking_app/booking.html", context)
    else:
        return redirect("/login/")


def my_bookings(request):
    """ A view to display the my bookings page and bookings """
    if request.user.is_authenticated:
        bookings = request.user.hiuser.all()
        context = {"bookings": bookings}
        return render(request, "booking_app/my-bookings.html", context)
    else:
        return redirect("/login/")


def edit_booking(request, booking_id):
    """ A view to edit booking and display the populated form """
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        messages.error(
            request, "This Booking does not exist or does not belong to you."
        )
        return redirect("my_bookings")
    else:
        if request.method == "POST":
            form = BookingForm(request.POST, instance=booking)
            bookings = request.user.hiuser.all()
            date_str = request.POST.get("date")
            form_date = parse_date(date_str)
            book_date = Booking.objects.filter(date=form_date)
            time_str = request.POST.get("time")
            book_time = Booking.objects.filter(time=time_str)
            today = str(date.today())
            if date_str >= today:
                if time_str != "Select a time":
                    if book_time and book_date:
                        if booking != form:
                            form = BookingForm()
                            context = {"bookings": bookings}
                            messages.error(
                                request,
                                "This time slot is taken,"
                                " please choose another time.",
                            )
                            return render(
                                request,
                                "booking_app/my-bookings.html",
                                context
                            )
                else:
                    form = BookingForm()
                    context = {"bookings": bookings}
                    messages.error(request, "Please Select a time! Try Again.")
                    return render(
                        request,
                        "booking_app/my-bookings.html",
                        context
                    )
            else:
                form = BookingForm()
                context = {"form": form}
                messages.error(
                    request,
                    "Please Select a present or future date."
                )
                return render(request, "booking_app/booking.html", context)
            if form.is_valid():
                form.save()
            messages.success(request, "Edit successful.")
            return redirect("my_bookings")
    form = BookingForm(instance=booking)
    context = {"form": form}
    return render(request, "booking_app/edit_booking.html", context)


def delete_booking(request, booking_id):
    """ A view to delete a booking """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Deletion successful.")
    return redirect("my_bookings")


def register_request(request):
    """ A view to display a registration form """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("my_bookings")
        messages.error(
            request,
            "Unsuccessful registration. Invalid information."
        )
    form = NewUserForm()
    return render(
        request=request,
        template_name="booking_app/register.html",
        context={"register_form": form},
    )


def login_request(request):
    """ A view to display a login form and allow user to login """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("my_bookings")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="booking_app/login.html",
        context={"login_form": form},
    )


def logout_request(request):
    """ A view to allow user to log out """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("booking_app")


def password_reset_request(request):
    """ A view to allow user to reset password via email """
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = (
                        "booking_app/password_reset_email.txt"
                    )
                    c_c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c_c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "support@geco-tech.net",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    messages.success(
                        request,
                        "A message with reset password"
                        " instructions has been sent to your inbox.",
                    )
                    return redirect("login")
            messages.error(request, "An invalid email has been entered.")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="booking_app/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
