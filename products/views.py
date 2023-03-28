from django.shortcuts import render
from products.models import Product


# Create your views here.



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


