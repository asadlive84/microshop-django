from django.db import models
from django.contrib.auth import get_user_model
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

    def __str__(self):
        return "Customer: %s" % self.name
