from django.shortcuts import render
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def cart(request):
    
    cart, created = Cart.objects.get_or_create(
        user = request.user,
        is_active = True
    )
    
    items = cart.items.select_related('product').all()
    
    context = {
        "cart": cart,
        "items": items
    }
    
    return render(request, "cart.html", context)


def checkout(request):
    return render(request, "checkout.html")