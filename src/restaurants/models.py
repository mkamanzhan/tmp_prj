from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, verbose_name="Name")
    short_description = models.CharField(max_length=250, verbose_name="Short description")
    description = models.TextField(verbose_name="Description")
    address = models.CharField(max_length=250, verbose_name="Address")
    is_active = models.BooleanField(default=True, verbose_name="Is active")
    rating = models.FloatField(verbose_name="Rating")
    logo = models.ImageField()


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Text")
