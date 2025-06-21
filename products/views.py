from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Product, Category
from django.db.models import Q
from django.contrib import messages
from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
from django.db.models import Q
from django.contrib import messages

def superuser_check(user):
    return user.is_superuser

def all_products(request):
    query = request.GET.get('q')  # Search query
    category = request.GET.get('category')  # Category filter
    sort = request.GET.get('sort')  # Sorting
    range_of_stars = range(1, 6)  # Star range for ratings
    
    # Start with all products
    products = Product.objects.all()
    
    # Apply search query if provided
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Apply category filter if provided
    if category:
        products = products.filter(category__name=category)
    
    
    # Apply sorting if provided
    if sort:
        if sort == 'low_to_high':
            products = products.order_by('price') # Sort by price (low to high)
        elif sort == 'high_to_low':
            products = products.order_by('-price') #Sort by price (high to low)
            print(products.query)  # Debug: Print the SQL query
        elif sort == 'name_a_z':
            products = products.order_by('name')  # Sort by name (A to Z)
        elif sort == 'name_z_a':
            products = products.order_by('-name')  # Sort by name (Z to A)
    
    # If no products are found, display a message
    if query and not products.exists():
        messages.error(request, 'No results found')

    # Prepare context for the template
    context = {
        'products': products,
        'range_of_stars': range_of_stars,
        'query': query,
        'selected_category': category,
        'selected_sort': sort
    }

    return render(request, 'products/products.html', context)



def product_detail(request,id):
    product= get_object_or_404(Product,pk=id)
    context = {
        'product':product
        
    }
    return render(request,'products/product_detail.html',context)




@user_passes_test(superuser_check)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('all_products')
        else:
            messages.error(request, 'Failed to add product')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@user_passes_test(superuser_check)
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('all_products')
        else:
            messages.error(request, 'Failed to update product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html',
            {'form': form, 'product': product})

@user_passes_test(superuser_check)
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('all_products')
    return render(request, 'products/delete_product.html',
            {'product': product})
    
    
   
