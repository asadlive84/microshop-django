from rest_framework import serializers
from accounts_app.models.account import Account, Customer
from accounts_app.models.ordered import Ordered
from accounts_app.models.customer_debit_credit import CustomerDebitCredit
from accounts_app.models.ordered import Ordered


class CustomerDebitCreditSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(many=False, read_only=True)
    customer_account = serializers.StringRelatedField(many=False)

    class Meta:
        model = CustomerDebitCredit
        fields = ['id', 'created_by', 'customer_account', 'customer_credit', 'customer_debit', 'created_at',
                  'customer_debit']


class OrderSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, many=False)
    customer = serializers.CharField(source="customer.name")

    class Meta:
        model = Ordered
        fields = ['created_by', 'customer', 'product_name', 'product_price', 'customer_paid', 'paid_status',
                  'unpaid_money',
                  'order_custom_date', 'extra_info', 'created_at', 'updated_at']


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
        fields = ['id', 'name', 'phone_number', 'address', 'created_at', 'paid_money', 'unpaid_money', 'paid_status',
                  'customer_credit', 'customer_debit', 'ac_last_updated', ]


class CustomerDetailSerializer(serializers.HyperlinkedModelSerializer):
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

    # customer = OrderSerializer(many=True)
    ordered_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='order-details',
    )

    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone_number', 'address', 'created_at', 'paid_money', 'unpaid_money', 'paid_status',
                  'customer_credit', 'customer_debit', 'ac_last_updated', 'ordered_set']
