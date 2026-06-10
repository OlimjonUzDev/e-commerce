import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .tasks import *
from .models import Order


@receiver(post_save, sender=Order)
def notify_admin(sender, inststance, created, **kwargs):
    if created:
        send_telegram_notification(
            order_id=inststance.id,
            product_name=inststance.product.name,
            quantity=inststance.quantity,
            customer_username=inststance.customer.username,
            phone_number=inststance.phone_number
        )