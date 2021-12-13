""" Import render """
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

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
    """ log in Page """
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
