from django.shortcuts import render
from rest_framework import generics
from accounts_app.models.account import Customer, Account
from accounts_app.rest.account_serializers import CustomerSerializer


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
