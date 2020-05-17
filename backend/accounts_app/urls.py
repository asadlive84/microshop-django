from django.urls import path, include
from accounts_app.views import CustomerListAPIView, CustomerDetailsAPIView, OrderListAPIView, OrderDetailAPIView, \
    CustomerDebitCreditAPIView, CustomerDebitCreditDetailsAPIView

urlpatterns = [
    path('customer_list/', CustomerListAPIView.as_view(), name="customer-list"),
    path('customer_list/<int:pk>/', CustomerDetailsAPIView.as_view(), name="customer-details"),
    path('order_list/', OrderListAPIView.as_view(), name="order-list"),
    path('order_list/<int:pk>/', OrderDetailAPIView.as_view(), name="order-details"),
    path('debit/', CustomerDebitCreditAPIView.as_view(), name="debit-credit"),
    path('debit/<int:pk>/', CustomerDebitCreditDetailsAPIView.as_view(), name="debit-credit-details"),
]
