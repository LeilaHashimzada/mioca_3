from django.urls import path

from .views import CartDetailView, CheckoutView
from order.views import update_item

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name = "cart"),
    path('checkout/', CheckoutView.as_view(), name = "checkout"),
    path("cart/update-item/", update_item, name="updat_-item")
]