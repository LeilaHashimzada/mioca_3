from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from product.models import Product,ProductCategory
from core.forms import ContactForm
from django.contrib import messages
from .models import Contact
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView, TemplateView

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    category_list = ProductCategory.objects.filter(parent__isnull=True)
    context = {
        "product_list" : product_list,
        "category_list" : category_list,
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
    return render(request, "about.html")


def faq(request):
    return render(request,'faq.html')

def code_404(request):
    return render(request, '404.html', status=404)

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    # context_object_name = 'formm'

    def form_valid(self, form):
        messages.add_message(self.request,messages.WARNING,"Successfully sent!")
        return super().form_valid(form)
    
   
    
