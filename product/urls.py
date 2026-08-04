from django.urls import path
from .views import compare, wishlist

urlpatterns = [
    path("compare/", compare, name="compare"),
    path("wishlist/", wishlist, name="wishlist")
]
