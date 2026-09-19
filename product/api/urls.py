from django.urls import path
from product.api.views import ProductColorListAPI, ProductSizeListAPI, ProductTagListAPI, categories,products,product_update,ProductListAPI,ProductUpdateDestroyAPIView

urlpatterns = [
    path('categories/', categories , name='categories'),
    path('tags/', ProductTagListAPI.as_view() , name='tags'),
    path('colors/', ProductColorListAPI.as_view() , name='colors'),
    path('sizes/', ProductSizeListAPI.as_view() , name='sizes'),
    path('products/',ProductListAPI.as_view(),name='products'),
    path('products/<int:pk>/',ProductUpdateDestroyAPIView.as_view(),name='product-update'),
]
