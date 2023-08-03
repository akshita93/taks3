from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

class User(AbstractUser):

    gender_choice = [
        ("male","Male"),
        ("female","Female"),
        ("other","Other")
    ]

    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10, choices=gender_choice)
    address=models.CharField(max_length=40,null=True,blank=True)
    landmark=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=30,null=True,blank=True)
    state=models.CharField(max_length=30,null=True,blank=True)
    city=models.CharField(max_length=30,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)