from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
from product.models import ProductTag

# Create your models here.
User = get_user_model()


class Blog(AbstractModel):
    user = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    tag = models.ManyToManyField(ProductTag, related_name="blogs", null=True, blank=True)
    image = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None, null = True, blank=True)


class BlogComment(AbstractModel):
    user =  models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, null = True, blank=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return self.blog.title
