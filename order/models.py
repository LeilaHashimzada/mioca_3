from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel
from product.models import Product
from core.validators import validate_country, validate_email

User = get_user_model()
# Create your models here.


class Cart(AbstractModel):
    user = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def price(self):
        total = 0
        for item in self.items.all():
            total += item.price()
        return total

    def quantity(self):
        total =0
        for item in self.items.all():
            total += item.quantity
        return total
            
    def __str__(self):
        return f"{self.user.first_name} cart"
    
    
class CartItem(AbstractModel):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ("cart", "product")
    
    def price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.cart.user.first_name
    
    
class OrderCheckout(AbstractModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null = True, blank=True)
    country = models.CharField(max_length=100, validators=[validate_country])
    street = models.CharField(max_length=50)
    appartment = models.CharField(max_length=50, null = True, blank=True)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField()
    zip = models.CharField(max_length=50, null = True, blank=True)
    note = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.first_name