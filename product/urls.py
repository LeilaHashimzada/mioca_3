from django.urls import path
from .views import compare, WishlistView, single_product,shop, update_item



urlpatterns = [
    path("compare/", compare, name="compare"),
    path("wishlist/", WishlistView.as_view(), name="wishlist"),
    path("shop/<int:pk>/", single_product, name="single_product"),
    path("shop/", shop, name="shop"),
    path("shop/update-item", update_item, name="update_item")
]
