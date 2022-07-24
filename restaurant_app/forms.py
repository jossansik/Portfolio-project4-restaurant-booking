from datetime import datetime, timedelta
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from restaurant_app.models import MIN_TABLE_CAPACITY, MAX_TABLE_CAPACITY

INTEGER_CHOICES = [tuple([choice, choice]) for choice in range(
    MIN_TABLE_CAPACITY, MAX_TABLE_CAPACITY+1)]


class BookingForm(forms.Form):
    reserved_start_date = forms.DateField(label='Choose a date', widget=DatePickerInput(format='%Y-%m-%d', options={
        'minDate': (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
        'maxDate': (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d'),
    }))
    num_guests = forms.CharField(
        label='Choose number of guests', widget=forms.Select(choices=INTEGER_CHOICES))
