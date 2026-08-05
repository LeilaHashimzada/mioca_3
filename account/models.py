from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    
class Account(models.Model):
    GENDER = {
        "Mr": "Mister",
        "Mrs": "Missis"
    }  
    gender = models.CharField(choices=GENDER)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    offers_receive = models.BooleanField(default=False)
    newsletter_sign_up = models.BooleanField(default=False)
    