""" Import render """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import BookingForm
from .forms import NewUserForm
from .models import Booking

# Create your views here.


def booking_app(request):
    """ Home Page """
    return render(request, 'BOOKING_APP/index.html')


def booking_view(request):
    """ Booking Page """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('my_bookings')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'BOOKING_APP/booking.html', context)


def my_bookings(request):
    """ My Bookings Page """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'BOOKING_APP/my-bookings.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
        return redirect('my_bookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'BOOKING_APP/edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('my_bookings')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("my_bookings")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="BOOKING_APP/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
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
    return render(request=request, template_name="BOOKING_APP/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("booking_app")
