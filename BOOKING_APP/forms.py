from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'device', 'message']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    device = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
