# Generated by Django 4.1.7 on 2023-04-16 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cartitems_remove_cart_is_ordered_cart_is_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]