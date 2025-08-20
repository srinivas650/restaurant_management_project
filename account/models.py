from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True,null=True)