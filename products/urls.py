from django.urls import path
from products.views import search

urlpatterns = [
    path('search', search, name="search")
]
