from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from .models import User
from order.models import Cart

def auth_view(request):
    register_form = RegisterForm()
    login_form = LoginForm()

    if request.method == 'POST':
        if 'register_submit' in request.POST:
            register_form = RegisterForm(data=request.POST)
            if register_form.is_valid():
                user = register_form.save()
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                return redirect('my_account', pk=user.id)
        elif "login_submit" in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = authenticate(
                    request, 
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password']
                )
                if user is not None:
                    login(request, user)
                    return redirect('my_account', pk=user.id)
            return redirect('404')

        elif "logout" in request.POST:
            logout(request)
            return redirect('homepage')
        
    context = {
        'register_form': register_form,
        'login_form': login_form
    }
    return render(request, "login.html", context)


class AccountView(DetailView):
    template_name = "my-account.html"
    model = User
    context_object_name = "person"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carts"] = Cart.objects.filter(user=self.request.user)
        return context



