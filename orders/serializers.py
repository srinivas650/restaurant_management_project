from rest_framework import serializers
from . models import Order,OrderItem
from home.models import MenuItem
class OrderItemSerializer(serializers.ModelSerializer):
    items=MenuItemSerializer(many=True,read_only=True)
    customer=serializers.StringRelatedField()
    class Meta:
        model=OrderItem
        fields=['product_name','quantity'.'price']

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['id','order_date','total_price','items']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['id','name','price']

