from django.urls import path
from shop.views import get_product, shop

urlpatterns = [
    path('<slug>/', get_product, name="get_product"),
    path('shop', shop, name="shop")
]
