from django.urls import path
from accounts.views import login_page, register_page
from django.contrib.auth import views

urlpatterns = [
   path('login/', login_page, name="login"),
   path('logout/', views.LogoutView.as_view, name="Logout"),
   path('register/', register_page, name="register")
]
