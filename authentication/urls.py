from django.urls import path
from . import views

urlpatterns = [
    
    path('register',views.registration,name='register'),
    path('admin_registration',views.adminregistration,name='admin_registration'),
    path('login',views.user_login,name='login'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('logout',views.user_logout,name='logout'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('admin_profile/<int:user_id>/', views.admin_profile, name='admin_profile'),
    path('profile',views.update_profile,name='profile'),

]