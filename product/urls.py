from django.urls import path
from .views import compare, wishlist,ListViewProduct,ShopDetailView



urlpatterns = [
    path("compare/", compare, name="compare"),
    path("wishlist/", wishlist, name="wishlist"),
    path("shop/<int:pk>/", ShopDetailView.as_view(), name="single_product"),
    path("shop/", ListViewProduct.as_view(), name="shop")
]
