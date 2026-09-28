from blog.models import Blog
from django.http import JsonResponse
from .serializer import BlogSerializer, BlogCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

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

class BlogListAPI(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogCreateSerializer
        return BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
class BlogListUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["UPDATE", "PUT"]:
            return BlogCreateSerializer
        return BlogSerializer  