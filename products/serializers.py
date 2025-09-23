from rest_framework import serializers
from .models import Item,MenuItems

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializers):
    class Meta:
        model=MenuItems
        fields=['id','name','price','category']