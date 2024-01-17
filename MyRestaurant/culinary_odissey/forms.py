from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    '''
   Form for handling reservation submissions.

   Attributes:
       name (CharField): Input field for the customer's name.
       email (EmailField): Input field for the customer's email address.
       phone (CharField): Input field for the customer's phone number.
       date (DateField): Input field for the reservation date.
       time (TimeField): Input field for the reservation time.
       people (IntegerField): Input field for the number of people in the reservation.

   Meta:
       model (Reservation): Specifies the model associated with the form.
       fields (tuple): List of fields to include in the form.
   '''
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Name'}
    ))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Email'}
    ))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your phone'}
    ))
    date = forms.DateField(label='Date', widget=forms.DateInput(
        attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'}
    ), input_formats=['%Y-%m-%d'])
    time = forms.TimeField(label='Time', widget=forms.TimeInput(
        attrs={'class': 'form-control timepicker', 'placeholder': 'HH:MM'}
    ), input_formats=['%I:%M%p', '%H:%M'])
    people = forms.IntegerField(label='People', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '#People'}
    ))

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'people')
