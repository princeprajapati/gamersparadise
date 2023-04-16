from django.urls import path
from accounts.views import login_page, register_page
from django.contrib.auth import views as auth_view


urlpatterns = [
   path('login/', login_page, name="login"),
   path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
   path('register/', register_page, name="register")
]
