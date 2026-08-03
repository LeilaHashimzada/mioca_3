from django.shortcuts import render

# Create your views here.
def index(request):
    return render('index', "index.html")

def about(request):
    return render("about", "about.html")

def contact(request):
    return render('contact', "contact.html")

def faq(request):
    return render('faq', "faq.html")