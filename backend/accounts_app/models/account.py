from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Customer(models.Model):
    """
    Customer Model
    """
    name = models.CharField("Name", max_length=100)
    phone_number = models.CharField("Mobile Number", max_length=100)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return "Customer: %s" % self.name

    def save(self, *args, **kwargs):
        """
        Create a new Account model object instance while created a new customer at Cutomer Table.
        """
        is_new = True if not self.id else False
        super(Customer, self).save(*args, **kwargs)
        if is_new:
            account = Account(customer=self)
            account.save()


class Account(models.Model):
    """
    Customer Account. One customer has only an account. This Table dont taken any input.
    It will be updated automatic.
    This table records customer paid or unpaid for alltime.
    """
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    paid_money = models.FloatField(blank=True, null=True)
    unpaid_money = models.FloatField(blank=True, null=True)
    paid_status = models.BooleanField(default=False)
    customer_credit = models.FloatField(blank=True, null=True)
    customer_debit = models.FloatField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Account Holder: %s" % self.customer.name

    def save(self, *args, **kwargs):
        self.unpaid_money = sum([item.unpaid_money for item in self.customer.ordered_set.all()])
        self.paid_money = sum([item.customer_paid for item in self.customer.ordered_set.all()])
        self.customer_credit = sum([x.customer_credit for x in self.customer.customerdebitcredit_set.all()]) + self.paid_money
        self.customer_debit = sum([x.customer_debit for x in self.customer.customerdebitcredit_set.all()]) + self.unpaid_money
        if self.customer_credit < self.customer_debit:
            self.paid_status = False
        elif self.customer_credit >= self.customer_debit:
            self.paid_status = True

        super().save(*args, **kwargs)
