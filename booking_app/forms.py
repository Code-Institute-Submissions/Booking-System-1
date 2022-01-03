from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking


DAYS_PICKER = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
]

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

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'device', 'message']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    time = forms.CharField(widget=forms.Select(choices=TIME_PICKER, attrs={'class': 'form-control'}))
    device = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class DayPicker(forms.ModelForm):
    
    time = [
        '09:00', '09:15', '09:30', '09:45',
        '10:00', '10:15', '10:30', '10:45',
        '11:00', '11:15', '11:30', '11:45',
        '12:00', '12:15', '12:30', '12:45',
        '13:00', '13:15', '13:30', '13:45',
        '14:00', '14:15', '14:30', '14:45',
        '15:00', '15:15', '15:30', '15:45',
        '16:00', '16:15', '16:30', '16:45',
        '17:00', '17:15', '17:30', '17:45',
        '18:00'
    ]