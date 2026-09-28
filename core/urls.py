from django.urls import path
from .views import index, about, faq, ContactView
from order.views import update_item

urlpatterns = [
    path('index/', index, name = "index"),
    path('about/', about, name = "about"),
    path('faq/', faq, name = "faq"),
    path('contact/', ContactView.as_view(), name = "contact"),
    path('update_item/', update_item, name="update_item")
]
