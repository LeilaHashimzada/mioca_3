from django.urls import path
from product.api.views import categories,products,product_update,ProductListAPI,ProductUpdateAPIView

urlpatterns = [
    path('categories/', categories , name='categories'),
    path('products/',ProductListAPI.as_view(),name='products'),
    path('product/<int:pk>/',ProductUpdateAPIView.as_view(),name='product-update'),
]