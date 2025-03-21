from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer


from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer