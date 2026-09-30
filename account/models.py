from django.db import models
from django.contrib.auth.models import AbstractUser
from core.validators import validate_email
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=True, validators=[validate_email])