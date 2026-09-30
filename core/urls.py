from django.urls import path
from .views import HomePageView, about, faq, ContactView, View404
from order.views import update_item

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name = "homepage"),
    path('about/', about, name = "about"),
    path('faq/', faq, name = "faq"),
    path('404/', View404.as_view(), name="NotFound"),
    path('contact/', ContactView.as_view(), name = "contact"),
    path('update_item/', update_item, name="update_item")
]
