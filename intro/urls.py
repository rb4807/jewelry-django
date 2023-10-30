from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('repair',views.repair,name='repair'),
    path('piercing',views.piercing,name='piercing'),
    path('polish',views.polish,name='polish'),
]

