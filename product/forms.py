from django import forms
from product.models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
            }),
        }
