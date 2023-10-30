from django.shortcuts import render

def home(request):
    return render(request, 'intro/index.html')

def repair(request):
    return render(request, 'intro/repair.html')

def piercing(request):
    return render(request, 'intro/piercing.html')

def polish(request):
    return render(request, 'intro/polish.html')

def about(request):
    return render(request, 'intro/about.html')