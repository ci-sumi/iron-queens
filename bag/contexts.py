from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Calculate and return the contents of the shopping bag,
    including total price, delivery charges, and
    free delivery threshold details.
    """
    bag_items = []
    total = Decimal('0.00')  # Use Decimal to prevent floating-point errors
    product_count = 0
    bag = request.session.get('bag', {})

    # Loop through each item in the shopping bag to calculate totals
    for item_id, item_quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        item_total = item_quantity * product.price
        total += item_total
        product_count += item_quantity  # Keep track of the product count
        # Append each item to the bag_items list
        bag_items.append({
            'item_id': item_id,
            'item_quantity': item_quantity,
            'product': product,
            'item_total': item_total,
        })

    # Delivery and free delivery threshold logic (calculated after the loop)
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = (
            total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
            / Decimal('100')
        )
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')  # No delivery charge for free delivery
        free_delivery_delta = Decimal('0.00')

    # Calculate grand total (total + delivery charge)
    grand_total = total + delivery

    # Return the context for rendering in the template
    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'FREE_DELIVERY_THRESHOLD': settings.FREE_DELIVERY_THRESHOLD,
    }
