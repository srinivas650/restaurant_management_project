from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    description=models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image=model.ImageField(upload_to='menuitem_images/',blank=True,null=True)


    def __str__(self):
        return str(self.item_name)
class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','pending'),
        ('CONFIRMED','confirmed'),
        ('DELIVERED','delivered'),
        ('CANCELLED','cancelled'),
    ]
    customer=models.Foreignkey(User,on_delete=models.CASCADE,related_name='orders')
    order_items=models.ManyToManyField(Item)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)
def CartItem(models.Model):
    user=models.Foreignkey(User,on_delete=models.CASCADE)
    item=models.Foreignkey(Item,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

class MenuCategory(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class MenuItems(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.Foreignkey(MenuCategory,on_delete=models.CASCADE,related_name='items')
    
    def __str__(self):
        return self.name



    