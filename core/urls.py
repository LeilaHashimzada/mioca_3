from django.urls import path
from .views import index, about, faq, ContactView

urlpatterns = [
    path('index/', index, name = "index"),
    path('about/', about, name = "about"),
    path('faq/', faq, name = "faq"),
    path('contact/', ContactView.as_view(), name = 'contact')
    
]
