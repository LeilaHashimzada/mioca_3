from django.contrib import admin
from .models import ProductCategory, Product, ProductPhoto, ProductReview, ProductTag, Wishlist
# Register your models here.


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1
    
class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoInline]
    
    
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(Wishlist)