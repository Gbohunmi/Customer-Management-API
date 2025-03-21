from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models

class CustomUserManager(BaseUserManager):
    # This method is used to create and save a regular user.
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #This method is used to create and save a superuser (an admin-level user with all permissions).
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None # Removed the username field
    email = models.EmailField(unique=True, blank=False) #Made email the unique identifier
    
    # Setting email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #The CustomUserManager is assigned to the custom user model through the objects attribute
    objects = CustomUserManager()


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




