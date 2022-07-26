from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser,PermissionsMixin):
    username=None
    email=models.EmailField(unique=True)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=[]

     
    objects = CustomUserManager()
    
    class Meta :
        ordering=['email']
        verbose_name='Users'

    def __str__(self):
        return self.email    