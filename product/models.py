from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel

User = get_user_model()

class ProductCategory(AbstractModel):
    parent = models.ForeignKey('self',related_name='child',on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to = "media", height_field=None, width_field=None, max_length=None,null=True)
    
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
        
class ProductColor(AbstractModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    @property
    def quantity(self):
        return self.products.count()
    
class ProductSize(AbstractModel):
    size = models.CharField(max_length=50)
    
    def __str__(self):
        return self.size
    
    @property
    def quantity(self):
        return self.products.count()
    
    
class Product(AbstractModel):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=False)
    is_added = models.BooleanField(default=False)
    information = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to = "media", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(ProductTag)
    color = models.ForeignKey(ProductColor, related_name="products", on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(ProductSize, related_name="products", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
    
class ProductPhoto(AbstractModel):
    photo = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    product_id = models.ForeignKey(Product, related_name="product_photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.title
    
    
class ProductReview(AbstractModel):
    name =  models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=50,null=True)
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)
    
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name="wishlist",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="wishlist",on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
    class Meta:
        verbose_name_plural = "Wishlist"


