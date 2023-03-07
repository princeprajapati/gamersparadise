from django.urls import path
from products.views import get_product, shop, checkout, category

urlpatterns = [
    path('<slug>/', get_product, name="get_product"),
    path('shop', shop, name="shop"),
    path('checkout', checkout, name="checkout"),
    path('shop', category, name="category")
]
