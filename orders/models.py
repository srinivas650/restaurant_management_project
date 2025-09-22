from django.db import models
from django.contrib.auth.models import User

class OrderStatus(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
class Coupon(models.Model):
    code=models.CharField(max_length=20,umique=True)
    idscount_percent=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

class Order(models.Model):
    user=models.ForiegnKey(User,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=255)
    order_date=models.DateTimeField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.ForiegnKey(OrderStatus,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'order #{self.id}-{self.customer_name}'
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product_name=models.CharField(max_length=200)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product_name}(x{self.quantity})"
        