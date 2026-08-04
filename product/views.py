from django.shortcuts import render

# Create your views here.

def compare(request):
    return render("compare", "compare.html")
    
def wishlist(request):
    return render("wishlist", "wishlist.html")