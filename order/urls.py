from django.urls import path

from .views import CartDetailView, checkout
from product.views import update_item

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name = "cart"),
    path('checkout/', checkout, name = "checkout"),
    path("cart/update-item/", update_item, name="update-item")
]