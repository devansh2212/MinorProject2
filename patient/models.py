from django.db import models
from .models import *
from django.contrib.auth.models import User

class Patient(models.Model):
	
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="")
	email = models.CharField(max_length=50,unique=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	age = models.IntegerField(default=0)  
	blood = models.CharField(max_length=10)
	username = models.OneToOneField(User,on_delete = models.CASCADE)
	def __str__(self):
		return f'{self.name}'
