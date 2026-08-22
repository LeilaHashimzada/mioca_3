from django.shortcuts import render
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
    return render("about", "about.html")

def contact(request):
    return render('contact', "contact.html")

def faq(request):
    return render(request,'faq.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "SUCCESS","Successfully sent!")
    context = {
        'form' : form
    }
    return render(request,'contact.html' ,context)

def code_404(request):
    return render(request, "404.html")