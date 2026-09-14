from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializer import ProductSerializer, ProductCreateSerializer
from product.models import Product
from django.http import JsonResponse

class ProductListApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(
            {"message": "Product created successfully", "data": serializer.data},
            status=200,
            headers=headers
        )
    
class ProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["PUT", 'PATCH']:
            return ProductCreateSerializer
        return ProductSerializer