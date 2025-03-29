from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CustomerModelViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = ['name', 'email']
    
    search_fields = ['name', 'email','address','phone_number']
    
    ordering_fields = ['name', 'created_at']


class OrderModelViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = ['customer', 'order_date', 'status', 'total']
    
    search_fields = ['customer']
    
    ordering_fields = ['customer', 'status', 'total']