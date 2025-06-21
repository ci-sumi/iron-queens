from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
# Create your models here.  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_validator = RegexValidator(
        regex=r'^\+?[\d\s\-]{7,15}$',
        message="Enter a valid phone number (e.g. +123456789 or 012-3456789)."
    )
    postcode_validator = RegexValidator(
        regex=r'^[A-Za-z0-9\s\-]{3,10}$',
        message="Enter a valid postal code (e.g. SW1A 1AA or 12345)."
    )

    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True,
        validators=[phone_validator]
    )
    default_county = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True,
        validators=[postcode_validator]
    )
    default_town_or_city = models.CharField(max_length=40, null=True,
    blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
    blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
    blank=True)
    default_country = CountryField(blank_label='Country', max_length=40,
    null=True, blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
    
class Contact(models.Model):
    ENQUIRY_TYPE = (
        ('product', 'Product Enquiry'),
        ('sales', 'Sales Enquiry'),
        ('service', 'Service Enquiry'),
        ('other', 'Other')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    enquiry_type = models.CharField(max_length=20, choices=ENQUIRY_TYPE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}-{self.get_enquiry_type_display()}" 
    
           
    
