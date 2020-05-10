from django.urls import path, include
from accounts_app.views import CustomerListAPIView,CustomerDetailsAPIView


urlpatterns = [
    path('customer_list/', CustomerListAPIView.as_view(), name="customer-list"),
    path('customer_list/<int:pk>/', CustomerDetailsAPIView.as_view(), name="customer-details"),
]
