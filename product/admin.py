from django.contrib import admin
from .models import ProductCategory, Product, ProductPhoto, ProductReview, ProductTag
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductPhoto)
admin.site.register(ProductReview)
admin.site.register(ProductTag)