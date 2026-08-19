from django.urls import path
<<<<<<< HEAD
from .views import cart, checkout, empty_cart

urlpatterns = [
    path('cart/', cart, name = "cart"),
    path('checkout/', checkout, name = "checkout"),
    path('empty_cart/', empty_cart, name = "empty_cart"),
  
=======
from .views import checkout, cart

urlpatterns = [
    path("checkout/", checkout, name='checkout'),
    path("cart/", cart, name='cart'),
    path("empty-cart/", cart, name = "empty_cart")
>>>>>>> origin/sugra
]
