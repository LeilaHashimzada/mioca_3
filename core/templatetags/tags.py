from django import template
from order.models import Cart, CartItem
from product.models import Wishlist

register = template.Library()

@register.simple_tag(takes_context=True)
def get_cart_items(context):
    request = context.get("request")

    if not request or not request.user.is_authenticated:
        return CartItem.objects.none()

    cart = Cart.objects.filter(user=request.user, is_active=True).first()

    if cart:
        return cart.items.select_related('product').all()
        
    return CartItem.objects.none()




@register.simple_tag(takes_context=True)
def get_wishlist_items(context):
    request = context.get("request")
    if not request or not request.user.is_authenticated:
        return Wishlist.objects.none()
    return Wishlist.objects.filter(user=request.user).select_related('product').all()