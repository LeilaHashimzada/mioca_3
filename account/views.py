from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm

# Create your views here.
def login(request):
    form = RegisterForm
    if request.method == 'POST':
            form =  RegisterForm(data=request.POST)
            print(request.POST)
            if form.is_valid():
                user = form.save()
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect(reverse_lazy('login'))
    context = {
        'form': form
    }
    return render(request, "login.html", context)

def account(request):
    return render(request,"my-account.html")

# def register(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form =  RegisterForm(data=request.POST)
#         print(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect(reverse_lazy('login'))
#     context = {
#         'form' : form
#     }
#     return render(request, "login.html", context)