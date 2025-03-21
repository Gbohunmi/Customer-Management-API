from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models

class CustomUser(AbstractUser):
    username = None # Removed the username field
    email = models.EmailField(unique=True, blank=False) #Made email the unique identifier
    
    # Setting email as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
