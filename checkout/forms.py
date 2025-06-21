from django import forms
from .models import Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
             'street_address1','street_address2',
             'town_or_city', 'postcode', 'county',
             'country',)
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Full Name *','autofocus': 'autofocus'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
             'placeholder': 'Email Address *'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Phone Number *'}),
            'street_address1': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Street Address 1 *'}),
            'street_address2': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Street Address 2 '}),
            'town_or_city': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Town or City *'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'Postcode '}),
            'county': forms.TextInput(attrs={'class': 'form-control',
             'placeholder': 'County, State or Province *'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control',
             'placeholder': 'Select Country'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    
        for field in self.fields.values():
            field.label = False