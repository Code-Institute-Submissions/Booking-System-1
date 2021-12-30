from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    """ Booking Form """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone = PhoneField(blank=True, null=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=False, blank=False)
    device = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, default='', null=True, on_delete=models.CASCADE, related_name='hiuser')

    def __str__(self):
        return f'{self.date} - {self.time} - {self.name}'
