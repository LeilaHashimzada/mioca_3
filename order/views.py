from django.shortcuts import render
from .models import Cart
from .forms import CheckoutFrom
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cart = Cart.objects.filter(user=self.request.user, is_active=True).first()
        
        context["cart"] = cart
        context["items"] = cart.items.select_related('product').all() if cart else []
        
        return context
    

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
