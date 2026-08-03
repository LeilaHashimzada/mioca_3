from django.db import models

# Create your models here.
class Newsletter:
    email = models.CharField(max_length=50)