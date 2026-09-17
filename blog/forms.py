from django import forms 
from .models import BlogComment, Blog

class BlogFrom(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = [
            "title", 
            "image",
            "tag",
            "content"
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Blog title"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "tag": forms.SelectMultiple(attrs={"class": "form-control", "size": "4"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Blog context"}),
        }

class BlogCommentForm(forms.ModelForm):
    
    class Meta:
        model = BlogComment
        fields = [
            "name",
            "email",
            "subject",
            "message"
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={
            "placeholder" : "Name *" 
            }),
            'email': forms.TextInput(attrs={
                "placeholder" : "Email *" 
            }),
            'subject': forms.TextInput(attrs={
            "placeholder" : "Subject (Optional)" 
            }),
            'message': forms.Textarea(attrs={
            "placeholder" : "Message" 
            }),
        }