from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem,Order

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    if created:
        instance.order.update_total()
        instance.update_order_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
    instance.order.update_order_total()
        