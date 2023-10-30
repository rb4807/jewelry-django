from django.urls import path
from . import views

urlpatterns = [
    path('sort/', views.sort_products, name='sort_products'),

]



