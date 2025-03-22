from django.urls import path
from .views import (CustomerListCreateAPIView,
                    CustomerRetrieveUpdateDestroyAPIView,
                    OrderListCreateAPIView,
                    OrderRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customers'),
    path('customer/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer'),
    path('orders/', OrderListCreateAPIView.as_view(), name='orders'),
    path('order/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order'),
]