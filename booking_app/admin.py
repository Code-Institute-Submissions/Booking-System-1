from django.contrib import admin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Admin Display Fields """
    list_display = ('name', 'date', 'time', 'email', 'device')
    search_fields = ('name', 'date', 'time', 'email', 'device')
