from django.urls import path
from .views import BlogListView, blog_single


urlpatterns = [
    path("blog/", BlogListView.as_view(), name = "blog"),
    path("blog/<int:pk>/", blog_single, name="single_blog")
]
