from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Product, ProductCategory,ProductReview,ProductTag
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from product.forms import ReviewForm
from .models import Wishlist
from django.contrib.auth.decorators import login_required

# Create your views here.
class ShopDetailView(FormMixin,DetailView):
    form_class = ReviewForm
    model = Product
    template_name = 'single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = self.get_form()
        context['item'] = self.object
        context['reviews'] = ProductReview.objects.filter(product=self.object)
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



def compare(request):
    return render(request, "compare.html")

class ListViewProduct(ListView):
    template_name = 'shop.html'
    model = Product
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        if category_id:
            queryset = queryset.filter(category=category_id)
        if tag_id:
            queryset = queryset.filter(tag=tag_id)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent = None)
        context['tags'] = ProductTag.objects.all()
        return context


@login_required

def addtowishlist(request,id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)

        Wishlist.objects.get_or_create(
            user=request.user,
            product=product,
        )

        return redirect("wishlist")

@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)


    context = {
        'items' : items
    }
    return render(request, 'wishlist.html', context)

@login_required
def removefromwishlist(request, id):
    if request.method == "POST":
        Wishlist.objects.filter(user=request.user, product_id=id).delete()
    return redirect("wishlist")


    
    