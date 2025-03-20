from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('user', 'User'),
        ('restaurant_owner', 'Restaurant Owner')
    )
    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    profile_image = models.ImageField(upload_to='profile/images', blank=True, null=True)
    