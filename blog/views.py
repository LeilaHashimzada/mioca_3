from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404



# Create your views here.
def blog(request):
    
    item = Blog.objects.all()
    
    context = {
        "blogs": item
    }
    
    return render(request, "blog.html", context)


def blog_single(request, pk):
    
    item = get_object_or_404(Blog, id = pk)
    
    context = {
        "blog": item
    }
    
    return render(request, "blog-single.html", context)