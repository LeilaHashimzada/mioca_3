from django.db import models

# Create your models here.
class Newsletter:
    email = models.CharField(max_length=50)

class AbstractModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contact(AbstractModel):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    context = models.TextField()

    def __str__(self):
        return self.name