from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',

        ]

        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control', 
                'placeholder' : 'Username'
            }),
            'email' : forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Email'
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            }),
           
        }