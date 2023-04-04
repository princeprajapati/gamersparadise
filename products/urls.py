from django.urls import path
from products.views import checkout, search

urlpatterns = [
    path('checkout', checkout, name="checkout"),
    path('search', search, name="search")
]
