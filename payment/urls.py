from django.urls import path
from . import views


urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('success', views.success, name='success'),
    path('booking', views.booking, name='booking'),
    path('charge', views.charge, name='charge'),
    path('error', views.error, name='error'),
    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment',views.payment.as_view(),name='payment')
]
