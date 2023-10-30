from django.urls import path
from . import views

urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('cancel_appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('working',views.working,name='working'),
    path('staff',views.staff,name='staff'),
    path('success',views.success,name='success'),

]
