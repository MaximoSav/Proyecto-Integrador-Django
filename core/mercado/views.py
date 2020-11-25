from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Producto, Destacado

# Create your views here.


def BaseView(request):
    if request.method == "POST":
        if 'search' in request.POST:
            form = BaseForm(request.POST)
            if form.is_valid():
                search_name = form.cleaned_data['search']
                productos = Producto.objects.filter(
                    nombre__icontains=search_name)
                return render(request, 'mercado/main.html', {'productos': productos, })
    else:
        form = BaseForm()
        productos = Producto.objects.all()
        destacados = Destacado.objects.all()
        return render(request, 'mercado/main.html', {'productos': productos, 'destacados': destacados, })


def registerView(request):
    if request.method == "POST":
        if 'search' in request.POST:
            form = BaseForm(request.POST)
            if form.is_valid():
                search_name = form.cleaned_data['search']
                productos = Producto.objects.filter(
                    nombre__icontains=search_name)
                return render(request, 'mercado/main.html', {'productos': productos, })
        else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.cliente.telefono = form.cleaned_data['telefono']
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.save()
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
