from django.shortcuts import render
from rest_framework import generics
from accounts_app.models.account import Customer, Account
from accounts_app.models.ordered import Ordered
from accounts_app.rest.account_serializers import CustomerSerializer, CustomerDetailSerializer, OrderSerializer, \
    CustomerDebitCreditSerializer
from accounts_app.models.customer_debit_credit import CustomerDebitCredit


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Ordered.objects.all()
    serializer_class = OrderSerializer


print(CustomerDetailsAPIView)


class OrderDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Ordered.objects.all()
    serializer_class = OrderSerializer


class CustomerDebitCreditAPIView(generics.ListAPIView):
    queryset = CustomerDebitCredit.objects.all()
    serializer_class = CustomerDebitCreditSerializer


class CustomerDebitCreditDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = CustomerDebitCredit.objects.all()
    serializer_class = CustomerDebitCreditSerializer
