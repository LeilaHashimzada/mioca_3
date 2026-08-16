from django.shortcuts import render

# Create your views here.
def cart(request):
    return render("cart", "cart.html")

def checkout(request):
    return render('checkout', "checkout.html")

def empty_cart(request):
    return render('empty_cart', "empty-cart.html")