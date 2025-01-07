from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,related_name="testimonials")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  f"{self.user.username} - {self.service.name}"
    
    