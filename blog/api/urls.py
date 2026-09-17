from django.urls import path
from blog.api.views import BlogListAPI, BlogListUpdateDeleteAPI

urlpatterns = [
    path('blogs/', BlogListAPI, name="blogs"),
    path('blogs/<int:pk>', BlogListUpdateDeleteAPI, name="blogs")
]
