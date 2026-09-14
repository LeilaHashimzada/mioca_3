from django.urls import path
from product.api.views import ProductListApiView, ProductUpdateAPIView

urlpatterns = [
    path('products/', ProductListApiView.as_view(), name="products"),
    path('products/<int:pk>', ProductUpdateAPIView.as_view(), name="products")
]
