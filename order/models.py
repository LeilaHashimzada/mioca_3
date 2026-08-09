from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel
from product.models import Product

User = get_user_model()
# Create your models here.


class Cart(AbstractModel):
    user = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.first_name} cart"
    
    
class CartItem(AbstractModel):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.cart.user.first_name
    
    
class OrderCheckout(AbstractModel):
    user = models.ForeignKey(User, related_name="checkout_form", on_delete=models.CASCADE)
    company = models.CharField(max_length=50, null=True, blank=True)
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