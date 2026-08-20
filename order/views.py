from django.shortcuts import render
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from .forms import CheckoutFrom
from django.contrib import messages

# Create your views here.

@login_required
def cart(request):
    
    cart, created = Cart.objects.get_or_create(
        user = request.user,
        is_active = True
    )
    
    items = cart.items.select_related('product').all()
    
    context = {
        "items": items
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
