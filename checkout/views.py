from django.shortcuts import render,redirect
from .forms import OrderForm
from django.contrib import messages
from bag.contexts import bag_contents
import stripe
from products.models import Product
from .models import Order, OrderLineItem
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data ={
            'full_name':request.POST['full_name'],
            'email':request.POST['email'],
            'phone_number':request.POST['phone_number'],
            'street_address1':request.POST['street_address1'],
            'street_address2':request.POST['street_address2'],
            'town_or_city':request.POST['town_or_city'],
            'postcode':request.POST['postcode'],
            'county':request.POST['county'],
            'country':request.POST['country'],
        }
        orderform = OrderForm(form_data)
        if orderform.is_valid():
            order = orderform.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect('checkout_success', order.order_number)
        
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            return redirect(reverse('checkout'))
        
        
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


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = Order.objects.get(order_number=order_number)
    # if request.user.is_authenticated:
    #     profile = request.user.profile
    #     order.user_profile = profile
    #     order.save()
    messages.success(request, f'Order successfully processed! \
        Your order number is . A confirmation \
        email will be sent to {order.email}.')
    if 'bag' in request.session:
        del request.session['bag']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
