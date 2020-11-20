from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def BaseView(request):
    return render(request, 'mercado/main.html', {'name': request.user, })


def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("base_url")
    else:
        return redirect("login_url")
