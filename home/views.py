from django.shortcuts import render,redirect
from django.conf import settings
from . models import RestaurantInfo
from . models import Feedback
from datetime import datetime
from django.db import DatabaseError
# Create your views here.
from . models import RestaurantInfo
def home(request):
    api_url='http://127.0.0.1:8000/api/menu'
    try:
        response=requests.get(api_url)
        menu_items=response.json()
        if  response.status_code==200 else []
    except Exception:
        menu_items=[]
    context={
        'restaurant_name':settings.RESTAURANT_NAME,
        'restaurant_address':settings.RES_PHONE_ADDRESS,
    }
    return render(request,'index.html',context)

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
def contact(request):
    contact_info={
        'phone':'8978556169',
        'email':'abc@gmail.com',
        'address':'Bengaluru',
    }
    return render(request,'contact.html',contact_info)
def index(request):
    restaurant=RestaurantInfo.objects.first()
    context={
        'restaurant_name':restaurant_name if restaurant else "our restaurant",
        'phone number':getattr(settings,'RES_PHONE_NUMBER','N/A')
    }
    return render(request,'index.html',context)
def feedback_view(request):
    error_message=None
    if request.method=='POST':
        comments=request.POST.get('comments')
        if comments:
            try:
                Feedback.objects.create(comments=comments)
            except DatabaseError as e:
                error_message='something went wrong'
    return render(request,'feedback.html'.{'error_messages':error_message})

def current_year(request):
    return {"current_year":datetime.now().year}