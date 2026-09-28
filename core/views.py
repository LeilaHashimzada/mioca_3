from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from product.models import Product,ProductCategory
from core.forms import ContactForm
from django.contrib import messages
from .models import Contact
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from product.models import Wishlist

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

def code_404(request):
    return render(request, '404.html', status=404)

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('contact')
    context_object_name = 'form'

    def form_valid(self, form):
        messages.add_message(self.request,messages.WARNING,"Successfully sent!")
        return super().form_valid(form)

@login_required
def add_to_wishlist(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)

        Wishlist.objects.get_or_create(
            user=request.user,
            product=product
        )

    return redirect("wishlist")
   

