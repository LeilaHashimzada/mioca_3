from django.shortcuts import render, redirect
from .models import Cart, OrderCheckout, CartItem
from product.models import Product
from .forms import CheckoutFrom
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin

class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cart = Cart.objects.filter(user=self.request.user, is_active=True).first()
        
        context["cart"] = cart
        context["items"] = cart.items.select_related('product').all() if cart else []
        
        return context
    

class CheckoutView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = "checkout.html"
    model = OrderCheckout
    form_class = CheckoutFrom
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user, is_active=True).first()
        items = CartItem.objects.filter(cart=cart)
        context['form'] = self.get_form()
        context['cart'] = cart
        context["items"] = items
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            
            
            cart = Cart.objects.filter(user=request.user, is_active=True).first()
            if cart:
                order.cart = cart
                cart.is_active = False
                cart.save(update_fields=['is_active'])
            
            order.save()
            
            messages.add_message(request, messages.SUCCESS, "Successfully sent!")
            return redirect('homepage')
        
        return self.render_to_response(self.get_context_data(form=form))
      
def update_item(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    
    product = Product.objects.get(id = productId)
    cart, _ = Cart.objects.get_or_create(user = request.user, is_active=True)
    cartItem, created = CartItem.objects.get_or_create(cart = cart, product= product)
   
    item_delete = False 
    
    if action == "add":
        if created:
            cartItem.quantity = 1
        else:
            cartItem.quantity += 1
        cartItem.save()
            
    elif action == "decrease":
        cartItem.quantity -=1
        if cartItem.quantity <=0:
            cartItem.delete()
            item_delete = True
        else:
            cartItem.save()
        
    elif action == "remove":
        cartItem.delete()
        item_delete = True

    else:
        return JsonResponse({"error": "Invalid action"}, status=400)
    
    return JsonResponse({
            "status": "success",
            "productId": product.id,
            "quantity": 0 if item_delete else cartItem.quantity,
            "itemDeleted": item_delete,
        }, status=200, safe=False)  