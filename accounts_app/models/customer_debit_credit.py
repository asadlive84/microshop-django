from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts_app.models.account import Customer
from accounts_app.models.models import Account

User = get_user_model()


class CustomerDebitCredit(models.Model):
    """
    If Customer has due money. Now customer give due money of any amount for increase her or his credit.
    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_account = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customerdebitcredit_set")
    customer_credit = models.FloatField()
    customer_debit = models.FloatField(default=0)
    extra_custom_date = models.DateTimeField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "credited: %s by %s " % (self.customer_credit, self.customer_account.account.customer.name)


@receiver(post_save, sender=CustomerDebitCredit)
def customer_debit_credit_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.customer_account.account.extra_info = "f"
        instance.customer_account.account.save()
