from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
TIME_PICKER = [
        ('09:00am', '09:00am'), ('09:15am', '09:15am'), ('09:30am', '09:30am'), ('09:45am', '09:45am'),
        ('10:00am', '10:00am'), ('10:15am', '10:15am'), ('10:30am', '10:30am'), ('10:45am', '10:45am'),
        ('11:00am', '11:00am'), ('11:15am', '11:15am'), ('11:30am', '11:30am'), ('11:45am', '11:45am'),
        ('12:00pm', '12:00pm'), ('12:15pm', '12:15pm'), ('12:30pm', '12:30pm'), ('12:45pm', '12:45pm'),
        ('13:00pm', '13:00pm'), ('13:15pm', '13:15pm'), ('13:30pm', '13:30pm'), ('13:45pm', '13:45pm'),
        ('14:00pm', '14:00pm'), ('14:15pm', '14:15pm'), ('14:30pm', '14:30pm'), ('14:45pm', '14:45pm'),
        ('15:00pm', '15:00pm'), ('15:15pm', '15:15pm'), ('15:30pm', '15:30pm'), ('15:45pm', '15:45pm'),
        ('16:00pm', '16:00pm'), ('16:15pm', '16:15pm'), ('16:30pm', '16:30pm'), ('16:45pm', '16:45pm'),
        ('17:00pm', '17:00pm'), ('17:15pm', '17:15pm'), ('17:30pm', '17:30pm'), ('17:45pm', '17:45pm')
    ]


class Booking(models.Model):
    """ Booking Form """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone = PhoneField(blank=True, null=False)
    date = models.DateField(null=False, blank=False)
    time = models.CharField(choices=TIME_PICKER, max_length=200)
    device = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, default='', null=True, on_delete=models.CASCADE, related_name='hiuser')

    def __str__(self):
        return f'{self.date} - {self.time} - {self.name}'
