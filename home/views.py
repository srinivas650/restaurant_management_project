from django.shortcuts import render,redirect
from django.conf import settings
from . models import RestaurantInfo
from . models import Feedback
from datetime import datetime
from django.db import DatabaseError
from . import ContactForm
# Create your views here.
from . models import RestaurantInfo
def home(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html',{'form':ContactForm()
        'restaurant_name':settings.RESTAURANT_NAME,
        'restaurant_address':settings.RES_PHONE_ADDRESS,
        })
        else:
            form=ContactForm()
            return render(request,'home.html',{
                'form':form,
                'restaurant_name':settings.RESTAURANT_NAME,
                'restaurant_address':settings.RES_PHONE_ADDRESS,

            })

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