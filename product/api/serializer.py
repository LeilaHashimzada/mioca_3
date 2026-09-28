from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag, ProductSize, ProductColor


class ProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='title',
        queryset=ProductCategory.objects.all(),
        required=False,
        allow_null=True
    )
    tag = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=ProductTag.objects.all(),
        required=False
    )
    color = serializers.SlugRelatedField(
        slug_field='name',
        queryset=ProductColor.objects.all(),
        required=False,
        allow_null=True
    )
    size = serializers.SlugRelatedField(
        slug_field='size',
        queryset=ProductSize.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'rating',
            'description',
            'information',
            'is_available',
            'is_added',
            'cover_image',
            'category',
            'tag',
            'color',
            'size',
        ]


class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'parent']


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ['id', 'name']


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id', 'size']


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    tag = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    color = serializers.SlugRelatedField(slug_field='name', read_only=True)
    size = serializers.SlugRelatedField(slug_field='size', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'category',
            'tag',
            'color',
            'size',
        ]