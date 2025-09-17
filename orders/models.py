from django.db import models

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