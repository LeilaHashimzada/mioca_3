from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path("blogs/", BlogListView.as_view(), name = "blogs"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="single_blog"),
    path("blogs/create/", BlogCreateView.as_view(), name="create_blog")
]
