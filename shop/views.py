from django.shortcuts import render
from products.models import Product, Category


# Create your views here.
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


def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, 'product/product.html', context={'product': product})
    except Exception as e:
        print(e)
