from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    ROLE_CHOICE = (
        'user', 'user',
        'restaurant_owner', 'restaurant_owner'
    )
    
    email = models.EmailField(unique=True, blank=False,null=False),
    phone_number = models.CharField(max_length=15, blank=True),
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='user'),
    profile_image = models.ImageField(upload_to='profile/images', blank=True, null=True)