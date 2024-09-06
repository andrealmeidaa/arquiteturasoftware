from django.dispatch import Signal

# This signal is sent at the time an order is placed
# https://docs.djangoproject.com/en/5.1/topics/signals/
order_placed = Signal(providing_args=['order'])

from django.db import models
from .signals import order_placed

class Order(models.Model):
    # Order fields
    # ...

    def save(self, *args, **kwargs):
        created = self.pk is None
        super().save(*args, **kwargs)
        if created:
            # Signal that an order has been placed
            order_placed.send(sender=self.__class__, order=self)

from django.dispatch import receiver
from .signals import order_placed

@receiver(order_placed)
def update_inventory(sender, order, **kwargs):
    # Logic to update inventory based on the order
    print(f"Inventory updated for order {order.pk}.")


#Outro ponto de notificação
from django.core.mail import send_mail
from django.dispatch import receiver
from .signals import order_placed

@receiver(order_placed)
def send_order_confirmation_email(sender, order, **kwargs):
    # Logic to send email
    send_mail(
        'Order Confirmation',
        f'Your order {order.pk} has been placed successfully.',
        'from@example.com',
        [order.customer_email],
        fail_silently=False,
    )

from django.apps import AppConfig

class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        import orders.signals 
