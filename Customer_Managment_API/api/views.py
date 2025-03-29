from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer


from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CustomerModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer