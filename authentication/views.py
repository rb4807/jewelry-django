from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, AdminProfile

# User Register

def registration(request):

    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        first_name = request.POST[ 'first_name']
        last_name = request.POST[ 'last_name']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username,first_name=first_name,last_name=last_name)
                UserProfile.objects.create(user=user,username=username,email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/register')
    else:   
        return render(request, 'authentication/register.html')

# user_login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile', user_id=user.id)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'authentication/login.html')

@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'explore/explore.html', {'user': user})

# user_logout

def user_logout(request):
    logout(request)
    return redirect('/explore')

# profile_view

@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'authentication/profile.html', {'user_profile': user_profile})

# update_profile

@login_required
def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        profile_photo = request.FILES.get('profile_photo')
        
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.username = username
        user_profile.email = email
        user_profile.profile_photo = profile_photo
        user_profile.save()
    
    return render(request, 'authentication/profile.html', {'user_profile': user_profile})

# Admin_register

def adminregistration(request):

    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        first_name = request.POST[ 'first_name']
        last_name = request.POST[ 'last_name']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('admin_registration')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('admin_registration')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username,first_name=first_name,last_name=last_name)
                AdminProfile.objects.create(user=user,username=username,email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('admin_login')
        else:
            messages.info(request,'Password not matching')
            return redirect('admin_registration')
        return redirect('/admin_registration')
    else:   
        return render(request, 'authentication/admin_registration.html')
    
# user_login

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_profile', user_id=user.id)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'authentication/admin_login.html')

@login_required
def admin_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'admin/adminhome.html', {'user': user})

# user_logout

def admin_logout(request):
    logout(request)
    return redirect('/explore')