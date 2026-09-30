from django.urls import path

from .views import CartDetailView, CheckoutView, OldCartView
from order.views import update_item

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name = "cart"),
    path('checkout/', CheckoutView.as_view(), name = "checkout"),
    path("cart/update-item/", update_item, name="updat_-item"),
    path("oldCart/<int:pk>", OldCartView.as_view(), name="old_cart"),
]