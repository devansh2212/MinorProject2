from django.db import models
from .models import *
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=12,default="")
    email=models.CharField(max_length=50,unique=True)
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=30,default="")
    Specializations=models.CharField(max_length=30,default="")

    def __str__(self):
        return f'{self.name}'
