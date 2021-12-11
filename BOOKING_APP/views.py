""" Import render """
from django.shortcuts import render


def booking_app(request):
    """ Home Page """
    return render(request, 'BOOKING_APP/index.html')


def booking_view(request):
    """ Booking Page """
    return render(request, 'BOOKING_APP/booking.html')

def log_in(request):
    """ log in Page """
    return render(request, 'BOOKING_APP/login.html')