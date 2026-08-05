from django.db import models

# Create your models here.

class Cart(models.Model):
    coupon = models.CharField(max_length=50, null=True)
    country = models.CharField()
    region = models.CharField()
    zip = models.CharField(max_length=50)
    shipping = models.CharField()

class OrderCheckout(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    country = models.CharField()
    street = models.CharField(max_length=50)
    appartment = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField()
    zip = models.CharField(max_length=50)
    accountCreate = models.BooleanField(default=False)
    note = models.TextField()
    addressDifference = models.BooleanField(default=False)
    