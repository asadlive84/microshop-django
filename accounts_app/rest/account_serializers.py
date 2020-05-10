from rest_framework import serializers
from accounts_app.models.account import Account, Customer
from accounts_app.models.customer_debit_credit import CustomerDebitCredit
from accounts_app.models.ordered import Ordered


class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer and Account two tables and relationships between one to one
    So I show one serializer file
    First I created field attributes for get Account Table attributes
    Then I add those attributes with Customer attributes.
    """
    paid_money = serializers.FloatField(source='account.paid_money')
    unpaid_money = serializers.FloatField(source='account.unpaid_money')
    paid_status = serializers.BooleanField(source='account.paid_status')
    customer_credit = serializers.FloatField(source='account.customer_credit')
    customer_debit = serializers.FloatField(source='account.customer_debit')
    ac_last_updated = serializers.DateTimeField(source='account.updated_at')

    class Meta:
        model = Customer
        fields = ['id','name', 'phone_number', 'address', 'created_at', 'paid_money','unpaid_money','paid_status','customer_credit','customer_debit','ac_last_updated']

# class CustomerAccountSerializer(serializers.ModelSerializer):
#     account = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Account
#         fields = ['account', 'paid_money', 'unpaid_money', 'paid_status', 'customer_credit', 'customer_debit', 'extra_info',
#                   'created_at', 'updated_at', ]
