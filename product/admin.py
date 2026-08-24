from django.contrib import admin
from .models import ProductCategory, Product, ProductPhoto, ProductReview, ProductTag
# Register your models here.


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1

class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoInline, ProductReviewInline]


admin.site.register(ProductCategory)
admin.site.register(ProductTag)


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "short_message", "product", "user", "created_at")
    list_filter = ("product", "created_at")
    search_fields = ("name", "email", "message")

    @admin.display(description="Message")
    def short_message(self, obj):
        return obj.message[:50]