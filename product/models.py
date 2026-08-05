from django.db import models
from account.models import Account
from core.models import AbstractModel


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Product Categories"
    

class Product(AbstractModel):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=False)
    information = models.TextField()
    review = models.TextField() 
    cover_image = models.ImageField(upload_to = "media", height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class ProductPhoto(AbstractModel):
    photo = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    product_id = models.ForeignKey(Product, related_name="product_photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.title
    
    
    
class ProductReview(AbstractModel):
    rating =  models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    product_id = models.ForeignKey(Product, related_name="product_reviews", on_delete=models.CASCADE)
    #user_id = models.ForeignKey(Account, related_name="user_review", on_delete=models.CASCADE)

    def __str__(self):
        return self.name