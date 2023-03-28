from django.shortcuts import render
from .cart import Cart


# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'Shop/menu_cart.html')

def cart(request):
    return render(request, 'Shop/cart.html')
