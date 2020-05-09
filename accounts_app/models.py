from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Customer(models.Model):
    name = models.CharField("Name", max_length=100)
    phone_number = models.CharField("Mobile Number", max_length=100)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Ordered(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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
        return "%s %s" % (self.product_name, self.customer.name)

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


class CustomerDebitCredit(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_account = models.ForeignKey("Account", on_delete=models.CASCADE)
    customer_credit = models.FloatField()
    customer_debit = models.FloatField(default=0)
    extra_custom_date = models.DateTimeField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_account.customer.name


class Account(models.Model):
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
        return self.customer.name

    def save(self, *args, **kwargs):
        self.unpaid_money = sum([item.unpaid_money for item in self.customer.ordered_set.all()])
        self.paid_money = sum([item.customer_paid for item in self.customer.ordered_set.all()])
        self.customer_credit = sum([x.customer_credit for x in self.customerdebitcredit_set.all()]) + self.paid_money
        self.customer_debit = sum([x.customer_debit for x in self.customerdebitcredit_set.all()]) + self.unpaid_money
        if self.customer_credit < self.customer_debit:
            self.paid_status = False
        elif self.customer_credit >= self.customer_debit:
            self.paid_status = True

        super().save(*args, **kwargs)


@receiver(post_save, sender=Ordered)
def order_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.customer.account.extra_info = "f"
        instance.customer.account.save()

@receiver(post_save, sender=CustomerDebitCredit)
def customer_debit_credit_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.customer_account.extra_info = "f"
        instance.customer_account.save()
