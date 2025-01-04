import logging
import stripe
import json
import time
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from products.models import Product
from .models import Order, OrderLineItem
from profiles.models import UserProfile

# Set up the logger
logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        logger.info(f"Unhandled webhook received: {event['type']}")
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_created(self, event):
        """Handle the payment_intent.created webhook from Stripe"""
        logger.info(f"Handling event: payment_intent.created")
        # This event doesn't have charge details yet, so we do not process payment details here.
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: No charge details available yet',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        logger.info(f"Handling event: payment_intent.succeeded")
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.get('bag')
        save_info = intent.metadata.get('save_info')

        # Initialize fields
        billing_details = None
        shipping_details = None
        grand_total = None

        try:
            # Retrieve the Charge object using the latest_charge from the PaymentIntent
            if intent.latest_charge:
                stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

                # Extract billing details from the Charge object
                billing_details = stripe_charge.billing_details
                shipping_details = intent.shipping
                grand_total = round(stripe_charge.amount / 100, 2)  # Convert amount to dollars (or applicable currency)
            else:
                raise ValueError("No charge details found in the PaymentIntent.")
        except Exception as e:
            logger.error(f"Error retrieving payment details: {e}")
            return HttpResponse(content=f'Error retrieving payment details: {e}', status=500)

        # Clean shipping details (removing empty values)
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
                
        profile = None
        username = intent.metadata.get('username')
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        # Check if the order already exists
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    user_profile=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        # If the order exists, we just send a confirmation email
        if order_exists:
            logger.info("Order already exists in the database.")
            # self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            logger.info("Creating new order.")
            order = None
            try:
                # Create a new order and associated order line items
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # Loop through the items in the bag to create line items for the order
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                logger.error(f"Error creating order: {e}")
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Send the confirmation email for the newly created order
        # self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        logger.error(f"Payment failed for event {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
