from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.contrib import messages
from bag.contexts import bag_contents
import stripe
from products.models import Product
from .models import Order, OrderLineItem
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile
from profiles.forms import UserProfileForm 
import json
from django.contrib.auth.models import AnonymousUser


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

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
            order = orderform.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
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
        return redirect('all_products')
    current_bag = bag_contents(request)
    total=current_bag['grand_total']
    stripe_total=round(total*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            orderform = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'town_or_city': profile.default_town_or_city,
                'postcode': profile.default_postcode,
                'county': profile.default_county,
                'country': profile.default_country,
            })
        except UserProfile.DoesNotExist:
            orderform = OrderForm()
    else:
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
    order = get_object_or_404(Order,order_number=order_number)
     #Handle anonymous and authenticated users
    if isinstance(request.user, AnonymousUser):
        profile = None  # No profile for anonymous users
    else:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
    
    if save_info:
        profile_data = {
            'default_full_name': order.full_name,
            'default_email': order.email,
            'default_phone_number': order.phone_number,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_town_or_city': order.town_or_city,
            'default_postcode': order.postcode,
            'default_county': order.county,
            'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
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
