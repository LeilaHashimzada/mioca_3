from django.contrib import admin
from .models import Blog, BlogComment

# Register your models here.

class BlogCommentInline(admin.TabularInline):
    model = BlogComment 
    extra = 1
    
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogCommentInline]
    list_display = ["id", "user", "title"]