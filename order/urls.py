from django.urls import path

from .views import cart, checkout

urlpatterns = [
    path('cart/', cart, name = "cart"),
    path('checkout/', checkout, name = "checkout"),
    path('empty_cart/', cart, name = "empty_cart"),
]