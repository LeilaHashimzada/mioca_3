from django.urls import path
from .views import compare, wishlist,single_product,shop

urlpatterns = [
    path("compare/", compare, name="compare"),
    path("wishlist/", wishlist, name="wishlist"),
    path("shop/<int:pk>/", single_product, name="single_product"),
    path("shop/", shop, name="shop")
]
