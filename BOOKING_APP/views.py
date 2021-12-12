""" Import render """
from django.shortcuts import render, redirect
from .models import Booking

# Create your views here.


def booking_app(request):
    """ Home Page """
    return render(request, 'BOOKING_APP/index.html')


def booking_view(request):
    """ Booking Page """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        Booking.objects.create(name=name, email=email, phone=phone, date=date, time=time, message=message)

        return redirect('my_bookings')
    return render(request, 'BOOKING_APP/booking.html')


def my_bookings(request):
    """ log in Page """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'BOOKING_APP/my-bookings.html', context)
