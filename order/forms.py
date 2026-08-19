from django import forms
from .models import OrderCheckout
from django.core.validators import ValidationError

class CheckoutFrom(forms.ModelForm):
    
    class Meta:
        model = OrderCheckout
        fields = [
            'first_name',
            'last_name',
            "company",
            "country",
            "street",
            "appartment",
            "city",
            "state",
            "zip",
            "phone",
            "email",
            "note"
        ]
        
        widgets = {
            'street': forms.TextInput(attrs={
                'class': 'billing-address',
                'placeholder': "House number and street name"
            }),
            'note': forms.Textarea(attrs={
                "placeholder" : "Notes about your order, e.g. special notes for delivery."
                })
        }
        
    def clean_email(self):
        value = self.cleaned_data['email']
        if not value.endswith("gmail.com"):
            raise ValidationError("Email must contain gmail.com")