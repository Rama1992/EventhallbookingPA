from django import forms
from .models import Reservations, EventHall
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from bootstrap_datepicker.widgets import DatePicker


class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = [
            'booked_on_date'
        ]
        widgets = {
            'booked_on_date': forms.SelectDateWidget()
        }


class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = [
            'booked_on_date',
            'booked_hall_name'
        ]
        widgets = {
            'booked_on_date': forms.SelectDateWidget(),
            'booked_hall_name': forms.Select()
        }


class AddEventHall(forms.ModelForm):
    class Meta:
        model = EventHall
        fields = [
            'name',
            'state',
            'city',
            'capacity',
            'image',
            'description',
            'phone_number'
        ]
        widgets = {
            'name': forms.TextInput(),
            'state': forms.TextInput(),
            'city': forms.TextInput(),
            'capacity': forms.NumberInput(),
            'image': forms.TextInput(),
            'description': forms.TextInput(),
            'phone_number': forms.NumberInput()
        }