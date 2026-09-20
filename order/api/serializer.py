from rest_framework import serializers
from order.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    
    title = serializers.CharField(source = "product.title")
    price = serializers.FloatField(source = "product.price")    
    
    class Meta:
        model=CartItem
        fields=["id", "title", "price", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source = "user.username")
    items = CartItemSerializer(many=True)
    
    class Meta:
        model=Cart
        fields = ["id", "username", "is_active", "items"]
        
class CartCreateSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source = "user.username")
    
    class Meta:
        model=Cart
        fields = ["id", "username", "is_active"]