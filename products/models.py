from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def clean_url(self):
        return self.slug.replace('', '-')

    def __str__(self) -> str:
        return self.category_name


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")

#
# class Cart(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
#     is_paid = models.BooleanField(default=False)
#
#
# class CartItems(BaseModel):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

#
# class Cart(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
#     items = models.ManyToManyField(Product, through='CartItem')
#
#     @property
#     def total_price(self):
#         total = 0
#         for item in self.cart_items.all():
#             total += item.total_price
#         return total
#
#     def __str__(self):
#         return f"Cart {self.uid}"
#
#
# class CartItem(BaseModel):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     @property
#     def total_price(self):
#         return self.quantity * self.product.price
#
#     def __str__(self):
#         return f"{self.quantity} of {self.product.product_name} in cart {self.cart.id}"
