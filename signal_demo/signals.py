import logging

from django.contrib.auth import user_logged_in, user_logged_out
from django.core.signals import request_finished
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete, m2m_changed
from django.dispatch import receiver

from signal_demo.models import Product


logger = logging.getLogger('data')


@receiver(pre_save, sender=Product)
def before_product_save(sender, instance, **kwargs):
    print(f"before_product_save: {instance.name}")
    logger.info(f"Product save: {instance.name}")


@receiver(post_save, sender=Product)
def after_product_save(sender, instance, created, **kwargs):
    if created:
        print(f"New product created: {instance.name}")
    else:
        print(f"Product updated: {instance.name}")


@receiver(pre_delete, sender=Product)
def before_product_delete(sender, instance, **kwargs):
    print(f"Product deleting: {instance.name}")


@receiver(post_delete, sender=Product)
def after_product_delete(sender, instance, **kwargs):
    print(f"Product deleted: {instance.name}")


@receiver(m2m_changed, sender=Product.categories.through)
def m2m_changed_handler(sender, instance, action, **kwargs):
    print(f"{instance.name}:category changed {action}")

@receiver(request_finished)
def request_finished(sender, **kwargs):
    print(f"HTTP request_finished ")


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    print(f"user_logged_in: {user.username}")


@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    print(f"user_logged_out: {user.username}")
