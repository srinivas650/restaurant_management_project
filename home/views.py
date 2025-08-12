from django.shortcuts import render

# Create your views here.
from . models import RestaurantInfo
def home(request):
    restaurant=RestaurantInfo.objects.first()
    return render(request,'index.html',{'restaurant_name':restaurant.name if restaurant else "our Restaurant"})
def about(request)