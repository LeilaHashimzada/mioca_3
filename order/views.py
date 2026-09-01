from django.shortcuts import render
from .models import Cart
from django.contrib.auth.decorators import login_required
from .forms import CheckoutFrom
from django.contrib import messages

@login_required
def cart(request):
    
    user_carts = Cart.objects.filter(user=request.user, is_active=True).order_by('id')
    
    if user_carts.exists():
        cart = user_carts.first()
        
        if user_carts.count() > 1:
            duplicate_carts = user_carts[1:]
            for dup_cart in duplicate_carts:
                dup_cart.items.update(cart=cart)
                dup_cart.delete()
    else:
        cart = Cart.objects.create(user=request.user, is_active=True)
    
    items = cart.items.select_related('product').all()
    
    context = {
        "cart": cart,
        "items": items,
    }
    
    return render(request, "cart.html", context)

def checkout(request):
    form = CheckoutFrom
    if request.method == "POST":
        form = CheckoutFrom(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully sent!")
        
    context = {
        "form": form
    }
    return render(request, "checkout.html", context)
