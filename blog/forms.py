from django import forms 
from .models import BlogComment

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