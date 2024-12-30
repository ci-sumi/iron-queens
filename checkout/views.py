from django.shortcuts import render,redirect
from .forms import OrderForm
from django.contrib import messages
from bag.contexts import bag_contents
import stripe
from django.conf import settings
# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect('products')
    current_bag = bag_contents(request)
    total=current_bag['grand_total']
    stripe_total=round(total*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)
    orderform = OrderForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')
    template = 'checkout/checkout.html'
    context = {
        'orderform':orderform,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret ,
    }
    return render(request, template, context)
