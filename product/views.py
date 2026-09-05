from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Product, ProductCategory,ProductReview
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from product.forms import ReviewForm

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

def wishlist(request):
    return render(request, "wishlist.html")

# def single_product(request,pk):
#     item = get_object_or_404(Product,id=pk)
#     review_form = ReviewForm()
#     if request.method == 'POST':
#         review_form = ReviewForm(data=request.POST)
#         if review_form.is_valid():
#             review = review_form.save(commit=False)
#             review.user = request.user
#             review.product = item
#             review.save()
#             messages.success(request, "Successful review!")
#             return redirect('single_product', pk=item.pk)
#     context = {
#         'item' : item,
#         'review_form' : review_form,
#     }
#     return render(request,"single-product.html" , context)


# def shop(request):
#     product_list = Product.objects.all()
#     categories = ProductCategory.objects.filter(parent = None)
    
#     context = {
#         "product_list" : product_list,
#         "categories" : categories
#     }
#     return render(request,"shop-left-sidebar.html", context)


class ListViewProduct(ListView):
    template_name = 'shop.html'
    model = Product
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent = None)
        return context

    
    