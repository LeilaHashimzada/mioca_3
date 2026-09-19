from rest_framework import serializers
from order.models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField("user.username")
    
    class Meta:
        model=Cart
        fields = ["username", "is_active"]
        
class CartCreateSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField("user.username")
    
    class Meta:
        model=Cart
        fields = ["username", "is_active"]