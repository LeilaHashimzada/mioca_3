from celery import shared_task
from .models import Contact
from product.models import Product
from mioca import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

email_list = Contact.objects.values_list('email', flat=True)
products = Product.objects.all()[:3]

@shared_task
def email_to_contact():
    subject = 'Latest Products'
    context = {
        'products': products
    }
    
    message = render_to_string('email_to_contact.html', context)
    
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'HTML'
    mail.send()