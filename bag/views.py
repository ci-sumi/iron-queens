from django.shortcuts import render,redirect ,get_object_or_404
from products.models import Product

# Create your views here.
def view_bag(request):
    return render(request,'bag/bag.html')


def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity', 1))
    if product_id in bag:
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity
        
        
    request.session['bag'] = bag
    return redirect('view_bag')


def update_bag(request, product_id):
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity',1))
        bag = request.session.get('bag', {})
        if new_quantity >0:
            bag[product_id] = new_quantity
        else:
            bag.pop(product_id,None)
            
    request.session['bag'] = bag
        
        
    return redirect('view_bag')
    