from django.shortcuts import render
from product.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.

def compare(request):
    return render(request, "compare.html")
    
def wishlist(request):
    return render(request, "wishlist.html")

def single_product(request,pk):

    try:
        item = get_object_or_404(Product,id=pk)
    except Http404:
        render(request, "404.html")
    else:
        context = {
            'item' : item
        }

    return render(request,"single-product.html" , context)


def shop(request):
    product_list = Product.objects.all()
    categories = ProductCategory.objects.filter(parent = None)
    
    context = {
        "product_list" : product_list,
        "categories" : categories
    }
    return render(request,"shop.html", context)


    