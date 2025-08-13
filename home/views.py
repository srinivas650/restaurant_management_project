from django.shortcuts import render

# Create your views here.
from . models import RestaurantInfo
def home(request):
    restaurant=RestaurantInfo.objects.first()
    return render(request,'index.html',{'restaurant_name':restaurant.name if restaurant else "our Restaurant"})
def about(request):
    return render(request,'about.html')

def menu_list(request):
    menu_items=[
        {'name':'Pizza','price':80},
        {'name':'Biryani','price':200},
        {'name':'Meals','price':100},
    ]
    context={
        'menu_list'=menu_items
    }
    return render(request,context)