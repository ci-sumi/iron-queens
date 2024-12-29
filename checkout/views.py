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
        'orderform':orderform,
        'stripe_public_key':'pk_test_51Qb2G9CONiVlUMPw7xwM5ot1cLkePj9I9dUB2PQcMK3WvmVpqyC8g9YFonHKM8aNGkqkOi3TRKjSffF3AN5dqBDL00PkSPbU2c',
        'client_secret': 'client_secret',
    }
    return render(request, template, context)