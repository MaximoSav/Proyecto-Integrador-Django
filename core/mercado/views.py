from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def BaseView(request):
    return render(request, 'mercado/base.html', {'name': request.user,})

@login_required
def dashboardView(request):
    return render(request, 'mercado/base.html')

def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})