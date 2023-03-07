from django.shortcuts import render
from products.models import Product,Category


# Create your views here.


def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, 'product/product.html', context={'product': product})
    except Exception as e:
        print(e)


def category(request):
    var = {'category': Category.objects.all()}
    return request, var


def checkout(request):
    return render(request, 'shop/checkout.html')


def shop(request):
    context = {'products': Product.objects.all()}
    return render(request, 'shop/shop.html', context)
