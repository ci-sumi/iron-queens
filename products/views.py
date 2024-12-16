from django.shortcuts import render,get_object_or_404
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


def product_detail(request,id):
    product= get_object_or_404(Product,pk=id)
    context = {
        'product':product
        
    }
    return render(request,'products/product_detail.html',context)