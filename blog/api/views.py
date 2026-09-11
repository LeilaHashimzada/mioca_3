from blog.models import Blog
from django.http import JsonResponse
from .serializer import BlogSerializer, BlogCreateSerializer
from rest_framework.decorators import api_view

@api_view(http_method_names= ['GET', 'POST'])
def blogs(request):
    blogs = Blog.objects.all()
    if request.method == 'POST':
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    
    serializer = BlogSerializer(blogs, many=True)
    return JsonResponse(data = serializer.data, safe = False)