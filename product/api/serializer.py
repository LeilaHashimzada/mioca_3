from rest_framework import serializers
from product.models import ProductCategory
from product.models import Product,ProductTag

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =[
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'category',
            'tag'
        ]

class ProductCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields =[
            'id',
            'title',
            'parent'
        ]

class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = [
            'id',
            'name'
        ]

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializers()
    tag = ProductTagSerializer(many= True)
    class Meta:
        model = Product
        fields =[
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'category',
            'tag'
        ]

