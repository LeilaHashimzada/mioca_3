from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Product, ProductCategory
from product.forms import ReviewForm

# Create your views here.

def compare(request):
    return render(request, "compare.html")

def wishlist(request):
    return render(request, "wishlist.html")

def single_product(request,pk):
    item = get_object_or_404(Product,id=pk)
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = item
            review.save()
            messages.success(request, "Successful review!")
            return redirect('single_product', pk=item.pk)
    context = {
        'item' : item,
        'review_form' : review_form,
    }
    return render(request,"single-product.html" , context)


def shop(request):
    product_list = Product.objects.all()
    categories = ProductCategory.objects.filter(parent = None)
    
    context = {
        "product_list" : product_list,
        "categories" : categories
    }
    return render(request,"shop-left-sidebar.html", context)


    