from rest_framework import serializers
from . models import RestaurantInfo,Table
class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=RestaurantInfo
        fields=['name']
    
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields=['table_number','capacity','is_available']

