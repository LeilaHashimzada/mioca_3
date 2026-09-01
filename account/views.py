from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def auth(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    if request.method == 'POST':
        if "register" in request.POST:
            register_form =  RegisterForm(data=request.POST)
            print(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                return redirect(reverse_lazy('my-account'))
        elif "login" in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                userAuthentificate = authenticate(request, username=login_form.cleaned_data['username'],
                                                    password=login_form.cleaned_data['password'])
            if userAuthentificate:
                login(request, userAuthentificate)
                return redirect(reverse_lazy('my-account'))
            else:
                return redirect(reverse_lazy('404'))
            
    context = {
        'register_form': register_form,
        'login_form': login_form
    }
    return render(request, "login.html", context)

def account(request):
    return render(request,"my-account.html")

