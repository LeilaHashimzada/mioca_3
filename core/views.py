from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from product.models import Product,ProductCategory
from core.forms import ContactForm
from django.contrib import messages
from .models import Contact
from django.views.generic import CreateView

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    category_list = ProductCategory.objects.filter(parent__isnull=True)
    context = {
        "product_list" : product_list,
        "category_list" : category_list,
    }

    return render(request, "index.html" , context)

def about(request):
    return render(request, "about.html")


def faq(request):
    return render(request,'faq.html')

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    # context_object_name = 'formm'

    def form_valid(self, form):
        messages.add_message(self.request,messages.WARNING,"Successfully sent!")
        return super().form_valid(form)
    
   
    
