from django.urls import path

from .views import CartDetailView, CheckoutView
from product.views import update_item

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name = "cart"),
    path('checkout/', CheckoutView.as_view(), name = "checkout"),
    path("cart/update-item/", update_item, name="update-item")
]