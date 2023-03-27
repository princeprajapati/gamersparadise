from django.shortcuts import render
from products.models import Product, Category


# Create your views here.

def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, 'product/product.html', context={'product': product})
    except Exception as e:
        print(e)


def search(request):
    if request.method == 'POST':
        searchedTerm = request.POST.get('game_search')
        if searchedTerm == "":
            return render(request, 'home/index.html')
        else:
            context = {'products': Product.objects.filter(product_name__contains=searchedTerm)}
            if context:
                return render(request, 'home/search.html', context)


def checkout(request):
    return render(request, 'shop/checkout.html')


def cart(request):
    return render(request, 'accounts/cart.html')


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)

    context = {'products': products,
               'categories': categories,
               'active_categories': active_category}
    return render(request, 'shop/shop.html', context)
