from django.shortcuts import render
from product.models import Product
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
    return render('faq', "faq.html")