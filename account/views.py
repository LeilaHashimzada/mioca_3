from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as djangologin

def auth_view(request):
    register_form = RegisterForm()
    login_form = LoginForm()

    if request.method == 'POST':
        if 'register_submit' in request.POST:
            register_form = RegisterForm(data=request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)  
                user.set_password(register_form.cleaned_data['password'])  
                user.save()  
                return redirect(reverse_lazy('login')) 
            
        elif 'login_submit' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                authenticate_user = authenticate(
                    request,
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password']
                )
                if authenticate_user:
                    djangologin(request, authenticate_user)
                    return redirect(reverse_lazy('index'))

    context = {
        'register_form': register_form,
        'login_form': login_form
    }
    return render(request, "login.html", context)


def account(request):
    return render(request,"my-account.html")



