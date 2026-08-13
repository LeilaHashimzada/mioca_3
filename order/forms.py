from django import forms
from .models import OrderCheckout

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