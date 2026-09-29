from django.urls import path
from blog.api.views import BlogListAPI, BlogListUpdateDeleteAPI

urlpatterns = [
    path('blogs/', BlogListAPI.as_view(), name="api_blogs"),
    path('blogs/<int:pk>', BlogListUpdateDeleteAPI.as_view(), name="api_blogs")
]
