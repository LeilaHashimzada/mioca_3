from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import (Product, ProductCategory,ProductReview,ProductTag,
                            Wishlist, ProductColor, ProductSize)
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from product.forms import ReviewForm
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from order.models import Cart, CartItem

# Create your views here.
class ShopDetailView(FormMixin, DetailView):
    form_class = ReviewForm
    model = Product
    template_name = 'single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = self.get_form()
        context['item'] = self.object
        context['reviews'] = ProductReview.objects.filter(product=self.object)
        context["products"] = Product.objects.filter(category=self.object.category)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        product = self.get_object()
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.product = product
            form.save()
            messages.success(request, "Successful review!")
            return redirect('single_product', pk=product.pk)
        return self.form_invalid(form)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.product = self.object
        review.save()

        messages.success(self.request, "Successful review!")
        return super().form_valid(form)

class CompareView(DetailView):
    template_name="compare.html"
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context["product"] = product
        context["related_products"] = Product.objects.filter(
            category=product.category
        ).exclude(pk=product.pk)[:2]
        return context   

class ListViewProduct(ListView):
    template_name = 'shop.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        
        sort_mapping = {
            'price_asc': 'price',     
            'price_desc': '-price',        
            'title_asc': 'title',          
            'title_desc': '-title',               
        }
        
        category_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        color_id = self.request.GET.get('color')
        size_id = self.request.GET.get("size")
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        
        sorting = self.request.GET.get('sort_by', 'default')
        
        if category_id:
            queryset = queryset.filter(category=category_id)
        if tag_id and tag_id.isdigit():
            queryset = queryset.filter(tag=tag_id)
        if color_id:
            queryset = queryset.filter(color=color_id)
        if size_id:
            queryset = queryset.filter(size=size_id)
        if min_price and max_price:
            queryset = queryset.filter(price__gte=float(min_price),price__lte=float(max_price))
        if sorting in sort_mapping:
            queryset = queryset.order_by(sort_mapping[sorting])
            
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent = None)
        context['tags'] = ProductTag.objects.all()
        context['colors'] = ProductColor.objects.all()
        context['sizes'] = ProductSize.objects.all()
        context["total_product_count"] = Product.objects.count()
        return context
    
    
    def get_paginate_by(self, queryset):
        show_option = self.request.GET.get('show', 20)
        try:
            return int(show_option)
        except ValueError:
            return 20


@login_required
def addtowishlist(request,id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)

        Wishlist.objects.get_or_create(
            user=request.user,
            product=product,
        )

    return redirect("wishlist")


#@login_required
class WishlistListView(ListView):
    template_name = "wishlist.html"
    model = Wishlist
    context_object_name = "items"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Wishlist.objects.filter(user=self.request.user)
        return context


@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    context = {
        "items": items
    }
    return render(request, "wishlist.html", context)

@login_required
def removefromwishlist(request, id):
    if request.method == "POST":
        Wishlist.objects.filter(user=request.user, product_id=id).delete()
    return redirect("wishlist")

@login_required
def update_item(request, pk=1):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    added_quantity = int(data.get("quantity", 1))
    
    product = Product.objects.get(id = productId)
    cart, created = Cart.objects.get_or_create(user = request.user, is_active=True)
    cartItem, created = CartItem.objects.get_or_create(cart = cart, product= product)
   
    item_delete = False 
    
    if action == "add":
        if created:
            cartItem.quantity = added_quantity
        else:
            cartItem.quantity += added_quantity
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
