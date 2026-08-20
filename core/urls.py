from django.urls import path
from .views import index, about, faq, contact

urlpatterns = [
    path('index/', index, name = "index"),
    path('about/', about, name = "about"),
    path('faq/', faq, name = "faq"),
    path('contact/', contact, name = "contact"),
    
]
