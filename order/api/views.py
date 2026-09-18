from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializer import CartSerializer, CartCreateSerializer
from order.models import Cart, CartItem

class CartListAPIView(ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.filter(is_active=True)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CartCreateSerializer
        return CartSerializer
    

class CartUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.filter(is_active=True)        
    
    def get_serializer_class(self):
        if self.request.method in ["UPDATE", "PUT"]:
            return CartCreateSerializer
        return CartSerializer