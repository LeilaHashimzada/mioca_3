from django.urls import path
from .views import checkout, cart

urlpatterns = [
    path("checkout/", checkout, name='checkout'),
    path("cart/", cart, name='cart'),
    path("empty-cart/", cart, name = "empty_cart")
]
