from django.shortcuts import render
from .models import Cart, OrderCheckout
from .forms import CheckoutFrom
from django.contrib import messages
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
    

class CheckoutView(FormMixin, TemplateView):
    template_name = "checkout.html"
    model = OrderCheckout
    form_class = CheckoutFrom
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user, is_active=True).first()
        context['form'] = self.get_form()
        context['cart'] = cart
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            
            cart = Cart.objects.filter(user=request.user, is_active=True).first()
            if cart:
                cart.is_active = False
                cart.save(update_fields=['is_active'])
            
            messages.add_message(request, messages.SUCCESS, "Successfully sent!")
            return
        
        return self.get(request, *args, **kwargs)
        