from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel

User = get_user_model()

class ProductCategory(AbstractModel):
    parent = models.ForeignKey('self',related_name='child',on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        if self.parent:
            return f'{self.parent.title}/{self.title}'
        return self.title
    
    class Meta:
        verbose_name_plural = "Product Categories"
    
        
class ProductTag(AbstractModel):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        

class Product(AbstractModel):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    is_available = models.BooleanField(default=False)
    is_added = models.BooleanField(default=False)
    information = models.TextField()
    cover_image = models.ImageField(upload_to = "media", height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete=models.CASCADE)
    tag = models.ManyToManyField(ProductTag)
    
    def __str__(self):
        return self.title
    
    
class ProductPhoto(AbstractModel):
    photo = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    product_id = models.ForeignKey(Product, related_name="product_photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.title
    
    
class ProductReview(AbstractModel):
    rating =  models.IntegerField()
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)
    
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


class Wishlist(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ManyToManyField(Product, related_name="wishlist")
    
    def __str__(self):
        return f"{self.user.username}-{self.product.title}"