from datetime import datetime, timedelta
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from restaurant_app.models import MIN_TABLE_CAPACITY, MAX_TABLE_CAPACITY

INTEGER_CHOICES = [tuple([choice, choice]) for choice in range(
    MIN_TABLE_CAPACITY, MAX_TABLE_CAPACITY+1)]


class BookingForm(forms.Form):
    reserved_start_date = forms.DateField(
        label='Choose a date',
        widget=DatePickerInput(format='%Y-%m-%d', options={
            'minDate': (datetime.today() + timedelta(days=1))
            .strftime('%Y-%m-%d'),
            'maxDate': (datetime.today() + timedelta(days=30))
            .strftime('%Y-%m-%d'),
        }))
    num_guests = forms.CharField(
        label='Choose number of guests',
        widget=forms.Select(choices=INTEGER_CHOICES))


class ReservationForm(forms.Form):
    guest_fullname = forms.CharField(
        label='Please enter your full name', required=True, max_length=150,
        widget=forms.TextInput(attrs={'placeholder': ''}))
    num_guests = forms.CharField(widget=forms.HiddenInput(), required=True)
    reserved_start_date = forms.DateField(
        widget=forms.HiddenInput(), required=True)
    table_id = forms.CharField(widget=forms.HiddenInput(), required=True)


class MyReservationForm(forms.Form):
    reservation_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=True)
