# Generated by Django 4.1.7 on 2023-02-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]