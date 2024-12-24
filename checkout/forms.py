from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
             'street_address1','street_address2',
             'town_or_city', 'postcode', 'county',
             'country',)
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your Full Name','autofocus': 'autofocus'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your phone number'}),
            'street_address1': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your street address1'}),
            'street_address2': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your street address2'}),
            'town_or_city': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your town or city'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your postcode'}),
            'county': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your county'}),
            'country': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Enter your country'}),
        }
            