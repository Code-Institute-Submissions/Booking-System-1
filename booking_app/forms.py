from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking


TIME_PICKER = [
    ("09:00am", "09:00am"),
    ("09:15am", "09:15am"),
    ("09:30am", "09:30am"),
    ("09:45am", "09:45am"),
    ("10:00am", "10:00am"),
    ("10:15am", "10:15am"),
    ("10:30am", "10:30am"),
    ("10:45am", "10:45am"),
    ("11:00am", "11:00am"),
    ("11:15am", "11:15am"),
    ("11:30am", "11:30am"),
    ("11:45am", "11:45am"),
    ("12:00pm", "12:00pm"),
    ("12:15pm", "12:15pm"),
    ("12:30pm", "12:30pm"),
    ("12:45pm", "12:45pm"),
    ("13:00pm", "13:00pm"),
    ("13:15pm", "13:15pm"),
    ("13:30pm", "13:30pm"),
    ("13:45pm", "13:45pm"),
    ("14:00pm", "14:00pm"),
    ("14:15pm", "14:15pm"),
    ("14:30pm", "14:30pm"),
    ("14:45pm", "14:45pm"),
    ("15:00pm", "15:00pm"),
    ("15:15pm", "15:15pm"),
    ("15:30pm", "15:30pm"),
    ("15:45pm", "15:45pm"),
    ("16:00pm", "16:00pm"),
    ("16:15pm", "16:15pm"),
    ("16:30pm", "16:30pm"),
    ("16:45pm", "16:45pm"),
    ("17:00pm", "17:00pm"),
    ("17:15pm", "17:15pm"),
    ("17:30pm", "17:30pm"),
    ("17:45pm", "17:45pm"),
    ("Select a time", "Select a time"),
]


class BookingForm(forms.ModelForm):
    """ A booking form """

    class Meta:
        model = Booking
        fields = [
            "name",
            "email",
            "phone",
            "date",
            "time",
            "device",
            "message"
        ]

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={"class": "form-control", "type": "date"})
    )
    time = forms.CharField(
        widget=forms.Select(
            choices=TIME_PICKER, attrs={"class": "form-control"}),
        initial="Select a time",
    )
    device = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class NewUserForm(UserCreationForm):
    """ A registration form """

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control requiredField"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control requiredField"}),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control requiredField", "type": "password"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control requiredField", "type": "password"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Password Confirmation"
