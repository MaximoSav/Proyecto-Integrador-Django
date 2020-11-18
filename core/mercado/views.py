from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def BaseView(request):
    return render(request, 'mercado/base.html', {'name': request.user,})

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'mercado/dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = UserCreationForm()

    return render(request, 'registro/register.html', {'form': form})

#def login(request):
 #   return render(request, 'registro/login.html')