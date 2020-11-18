from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def BaseView(request):
    return render(request, 'mercado/base.html', {'name': request.user,})

def dashboardView(request):
    return render(request, 'mercado/dashboard.html')

def registerView(request):
    return render(request, 'registration/register.html')

def login(request):
    return render(request, 'registration/login.html')