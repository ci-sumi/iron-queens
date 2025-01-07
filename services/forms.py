from django import forms
from .models import Service,Testimonial

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields =['name', 'description', 'image']
        
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields =['service', 'content']
    
    
