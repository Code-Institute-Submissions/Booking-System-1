""" Import render """
from django.shortcuts import render
from .models import Booking

# Create your views here.


def booking_app(request):
    """ Home Page """
    return render(request, 'BOOKING_APP/index.html')


def booking_view(request):
    """ Booking Page """
    return render(request, 'BOOKING_APP/booking.html')


def my_bookings(request):
    """ log in Page """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'BOOKING_APP/my-bookings.html', context)
