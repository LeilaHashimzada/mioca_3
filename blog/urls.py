from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path("blog/", BlogListView.as_view(), name = "blog"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="single_blog"),
    path("blog/create/", BlogCreateView.as_view(), name="create_blog")
]
