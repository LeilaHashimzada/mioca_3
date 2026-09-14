from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'context',

        ]

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control' 
            }),
            'email' : forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'context' : forms.Textarea(attrs={
                'class' : 'form-control'
            }),
        }