from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    name=models.CharField(max_length=255)

class RestaurantLocation(models.Model):
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    opening_hours=models.JSONField(default=dict)

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    comments=models.TextField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mesaage=models.TextField()
    phone=models.IntegerField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    
