from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('admin', 'Admin'),
    )
    is_active= models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
