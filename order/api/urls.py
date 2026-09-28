from django.urls import path
from .views import CartListAPIView, CartUpdateDestroyAPIView

urlpatterns = [
    path("carts/", CartListAPIView.as_view(), name="carts"),
    path("carts/<int:pk>", CartUpdateDestroyAPIView.as_view(), name="carts"),
]
