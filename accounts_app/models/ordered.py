from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts_app.models.account import Customer

User = get_user_model()


class Ordered(models.Model):
    """
    Order Model of each customer. Customer has taken many orders and pay any amount or unpaid.
    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ordered_set')
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    customer_paid = models.FloatField(default=0)
    paid_status = models.BooleanField(blank=True)
    unpaid_money = models.FloatField(blank=True)
    order_custom_date = models.DateTimeField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s price: %s TK, Paid: %s TK Unpaid %s" % (self.product_name, self.product_price, self.customer_paid, self.unpaid_money)

    def save(self, *args, **kwargs):
        if self.product_price == self.customer_paid:
            self.paid_status = True
            self.unpaid_money = 0
        elif self.product_price > self.customer_paid:
            self.paid_status = False
            self.unpaid_money = self.product_price - self.customer_paid

        if self.customer_paid > self.product_price:
            raise ValueError("Not allowed. Customer paid too much!")

        super().save(*args, **kwargs)


@receiver(post_save, sender=Ordered)
def order_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.customer.account.extra_info = "f"
        instance.customer.account.save()
