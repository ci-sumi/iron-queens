from django.shortcuts import render,get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.contrib import messages



# Create your views here.
def all_products(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    products = Product.objects.all()
    range_of_stars = range(1,6)
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query))
    if not products.exists():
        messages.error(request,'No results found')
    if category:
        products = Product.objects.filter(category__name=category)
    context = {
        'products':products,
        'range_of_stars':range_of_stars,
        'query':query,
        'selected_category':category
    }
    return render(request,'products/products.html',context)


def product_detail(request,id):
    product= get_object_or_404(Product,pk=id)
    context = {
        'product':product
        
    }
    return render(request,'products/product_detail.html',context)