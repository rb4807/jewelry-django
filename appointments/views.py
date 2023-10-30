from django.shortcuts import render, redirect
from .models import Appointment,Staff,Working
from .forms import AppointmentForm, CancelAppointmentForm

def staff(request):
    staff = Staff.objects.all()
    return render(request, 'appointments/staff.html',{'staff' :staff})

def working(request):
    working = Working.objects.all()
    return render(request, 'appointments/working.html',{'working' :working})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'appointments/success.html',)
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/book_appointment.html', {'form': form})

def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        form = CancelAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = CancelAppointmentForm(instance=appointment)
    return render(request, 'appointments/cancel_appointment.html', {'form': form, 'appointment': appointment})

def success(request):
    return render(request, 'appointments/success.html')

def appointment_list(request):
    appointments = Appointment.objects.filter(canceled=False)
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})
