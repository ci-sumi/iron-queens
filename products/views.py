from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    range_of_stars = range(1,6)
    context = {
        'products':products,
        'range_of_stars':range_of_stars
    }
    return render(request,'products/products.html',context)