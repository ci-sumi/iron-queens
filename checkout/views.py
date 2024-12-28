from django.shortcuts import render,redirect
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect('products')
    orderform = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'orderform':orderform
    }
    return render(request, template, context)