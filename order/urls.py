from django.urls import path

from .views import CartDetailView, checkout

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name = "cart"),
    path('checkout/', checkout, name = "checkout"),
    path('empty_cart/', CartDetailView.as_view(), name = "empty_cart"),
]