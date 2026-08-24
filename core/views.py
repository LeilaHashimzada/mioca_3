from django.shortcuts import render, redirect
from product.models import Product
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {
        "product_list" : product_list,
    }

    return render(request, "index.html" , context)


def about(request):
    return render(request, "about.html")

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully sent!")
            return redirect('contact')
    context = {
        'form' : form
    }
    return render(request,'contact.html' ,context)

def faq(request):
    return render(request,'faq.html')