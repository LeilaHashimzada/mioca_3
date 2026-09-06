from django.shortcuts import render
from product.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from django.http import Http404
import json
from django.http import JsonResponse
from order.models import Cart, CartItem
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


def update_item(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    
    product = Product.objects.get(id = productId)
    cart, created = Cart.objects.get_or_create(user = request.user, is_active=True)
    cartItem, created = CartItem.objects.get_or_create(cart = cart, product= product)
    
    if action == "add":
        if created:
            cartItem.quantity = 1
        else:
            cartItem.quantity += 1
    elif action == "decrease":
        cartItem.quantity -=1
    elif action == "remove":
        cartItem.delete()
        
            
    cartItem.save()
    return JsonResponse(data, safe=False)