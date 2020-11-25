from django.shortcuts import redirect
from mercado.models import *
from django.contrib.auth.decorators import login_required
from .cart import Cart

# Create your views here.


@login_required(login_url="/autentication/login")
def add_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(Producto=product)
    return redirect('/carrito/')


@login_required(login_url="/autentication/login")
def remove_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.remove(Producto=product)
    return redirect('/carrito/')


@login_required(login_url="/autentication/login")
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.decrement(product)
    return redirect('/carrito/')


@login_required(login_url="/autentication/login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
