from django.urls import path
from accounts.views import login_page, register_page
from django.contrib.auth import views as auth_view
from accounts.views import add_to_cart,cart_view


urlpatterns = [
   path('login/', login_page, name="login"),
   path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
   path('register/', register_page, name="register"),
   path('add-to-cart/<uid>/', add_to_cart, name='add_to_cart'),
   path('cart/', cart_view, name='cart')
]
