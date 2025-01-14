from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100, unique=True )
    friendly_name = models.CharField(max_length=100,blank=True , null=True)
    
    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name
    

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    # image = CloudinaryField('image', null=True, blank=True) 
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    