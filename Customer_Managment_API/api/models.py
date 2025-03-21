from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models

class CustomUser(AbstractUser):
    username = None # Removed the username field
    email = models.EmailField(unique=True, blank=False) #Made email the unique identifier
    
    # Setting email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

class Customer(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField()
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date    = models.DateTimeField(auto_now_add=True)
    status        = models.CharField(max_length=20, choices=[
                        ('unpaid', 'Unpaid'),
                        ('paid', 'Paid'),
                     ])
    total  = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} for {self.customer} made at {self.order_date}"

