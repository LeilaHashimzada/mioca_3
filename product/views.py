from django.shortcuts import render
from product.models import Product

# Create your views here.

def compare(request):
    return render(request, "compare.html")
    
def wishlist(request):
    return render(request, "wishlist.html")

def single_product(request):
    return render(request,"single-product.html")

def shop(request):
    product_list = Product.objects.all()
    context = {
        "product_list" : product_list,
    }
    return render(request,"shop-left-sidebar.html",context)
