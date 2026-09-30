from django.shortcuts import render
from .models import Blog
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import BlogCommentForm, BlogFrom
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

class BlogListView(ListView):
    template_name = "blog.html"
    context_object_name = "blogs"
    model = Blog
    paginate_by = 3

class BlogDetailView(DetailView, FormMixin):
    template_name = "blog-single.html"
    context_object_name = "blog"
    model = Blog
    form_class = BlogCommentForm
    success_url = reverse_lazy('blogs')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        blog = self.get_object()
        if form.is_valid():
            form.instance.blog = blog
            if self.request.user.is_authenticated:
                form.instance.user = self.request.user
                
            form.save()
        return super().form_valid(form)
    
    
class BlogCreateView(CreateView):
    template_name="create-blog.html"
    form_class=BlogFrom
    model = Blog
    success_url=reverse_lazy("blogs")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    

#messages.add_message(request, messages.SUCCESS, "Successfully sent!")
        