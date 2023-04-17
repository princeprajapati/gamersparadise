from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from products.models import Product, Category
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)

    # profile_image = models.ImageField(upload_to='profile')

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid=False, cart__user=self.user).count()

    def cart_count(self):
        return self.get_cart_count()

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    is_paid = models.BooleanField(default=False)


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

