from django.contrib import admin
from accounts_app.models import Customer, Account, Ordered, CustomerDebitCredit


admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Ordered)
admin.site.register(CustomerDebitCredit)
