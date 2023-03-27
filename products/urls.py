from django.urls import path
from products.views import get_product, shop, checkout, cart, search

urlpatterns = [
    path('<slug>/', get_product, name="get_product"),
    path('shop', shop, name="shop"),
    path('checkout', checkout, name="checkout"),
    path('cart', cart, name="cart"),
    path('search', search, name="search")
]
