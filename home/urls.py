from django.urls import path
from home.views import index, contact, about
from accounts.views import login_page, register_page

urlpatterns = [
    path('', index, name="index"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('contact', contact, name="contact"),
    path('about', about, name="about")
]
