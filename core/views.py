from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from product.models import Product
from .models import Contact
from core.forms import ContactForm
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {
        "product_list" : product_list,
    }

    return render(request, "index.html" , context)

class ContactView(TemplateView, FormMixin):
    template_name = "contact.html"
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contact")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "SUCCESS","Successfully sent!")
            return
        
        return self.get(request, *args, **kwargs)

def about(request):
    return render("about", "about.html")

def faq(request):
    return render(request,'faq.html')

def code_404(request):
    return render(request, "404.html")