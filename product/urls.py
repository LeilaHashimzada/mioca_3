from django.urls import path
from .views import compare, wishlist,ListViewProduct,ShopDetailView,addtowishlist,removefromwishlist, update_item



urlpatterns = [
    path("compare/", compare, name="compare"),
    path("wishlist/", wishlist, name="wishlist"),
    path("wishlist/add/<int:id>/", addtowishlist, name="add_to_wishlist"),
    path("shop/<int:pk>/", ShopDetailView.as_view(), name="single_product"),
    path("shop/", ListViewProduct.as_view(), name="shop"),
    path("wishlist/remove/<int:id>/", removefromwishlist, name="remove_from_wishlist"),
    path("shop/<int:pk>/update-item/", update_item, name="update_item"),
]
