from django.urls import path
from .views import index, about, faq, ContactView, code_404

urlpatterns = [
    path('index/', index, name = "index"),
    path('about/', about, name = "about"),
    path('faq/', faq, name = "faq"),
    path('contact/', ContactView.as_view(), name = "contact"),
    path('PageNotFound/', code_404, name="404")
    
]
