from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Cart, CartItems


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account is not verified.')
        #     return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return render(request, 'home/index.html')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'Registered Successfully')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')


@login_required
def add_to_cart(request, uid):
    product = Product.objects.get(uid=uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    cart_item = CartItems.objects.create(cart=cart, product=product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_view(request):
    cart_items = CartItems.objects.filter(cart__user=request.user, cart__is_paid=False)
    total_price = sum(item.product.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    print(context)
    return render(request, 'Shop/cart.html', context)


def checkout(request):
    cart_items = CartItems.objects.filter(cart__user=request.user, cart__is_paid=False)
    total_price = sum(item.product.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'Shop/checkout.html', context)

