from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import BlogCommentForm


# Create your views here.
def blog(request):
    
    item = Blog.objects.all()
    
    context = {
        "blogs": item
    }
    
    return render(request, "blog.html", context)

@login_required
def blog_single(request, pk):
    
    try:
        item = get_object_or_404(Blog, id = pk)
    except Http404:
        return render(request, "404.html")
    else:
        form = BlogCommentForm
        if (request.method == "POST"):
            form = BlogCommentForm(data = request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = item
                comment.user = request.user
                comment.save()
        context = {
            "blog": item,
            "form": form
        }
        return render(request, "blog-single.html", context)