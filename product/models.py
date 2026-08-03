from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Product Categories"
        
class ProductPhoto:
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    
class Review:
    rating =  models.IntegerField(choices=[1,2,3,4,5])
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

class Product:
    title = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.IntegerField(choices=[1,2,3,4,5])
    description = models.TextField()
    is_available = models.BooleanField(default=False)
    information = models.TextField()
    review = models.ForeignKey(Review, related_name="products", on_delete=models.CASCADE)
    photo = models.ForeignKey(ProductPhoto, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title