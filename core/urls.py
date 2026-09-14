from django.urls import path
from .views import index, about, faq, ContactView, code_404
from order.views import update_item

urlpatterns = [
    path('index/', index, name = "index"),
    path('about/', about, name = "about"),
    path('faq/', faq, name = "faq"),
    path('contact/', ContactView.as_view(), name = "contact"),
    path('PageNotFound/', code_404, name="404"),
    path('update_item/', update_item, name="update_item")
]
