from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"