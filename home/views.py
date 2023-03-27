from django.shortcuts import render
from products.models import Product


# Create your views here.


def index(request):
    if request.GET.get('game_search'):
        search_context = {'search': Product.objects.filter()}
    context = {'products': Product.objects.all()}
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

