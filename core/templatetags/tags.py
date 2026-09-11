from django import template
from order.models import Cart, CartItem


register = template.Library()

@register.simple_tag(takes_context=True)
def get_cart_items(context):
    request = context.get("request")

    if not request or not hasattr(request, 'user') or not request.user.is_authenticated:
        return CartItem.objects.none()

    cart = Cart.objects.filter(user=request.user, is_active=True).first()

    if cart:
        return cart.items.select_related('product').all()
        
    return CartItem.objects.none()