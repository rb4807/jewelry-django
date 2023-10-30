from django import forms
from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date' 

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'customer' ,'staff']
        
        widgets = {
            'date': DateInput(),
        }

class CancelAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['canceled']

    

    labels = {
        'staff' : "Staff:",
        'date': "Appointment Date:",
        'customer' : "Name:",
    }