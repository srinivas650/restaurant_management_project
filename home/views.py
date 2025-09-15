from django.shortcuts import render,redirect
from django.conf import settings
from . models import RestaurantInfo
from . models import Feedback
from datetime import datetime
from django.db import DatabaseError
from . import ContactForm
from django.core.mail. import send_mail
from django.contrib import messages
from . forms import FeedbackForm
# Create your views here.

from . models import RestaurantInfo,RestaurantLocation
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
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['message']
            subject=f"New Contact Form Submission from {name}"
            body=f"Message from {name} {{email}:\n\n{message}}"
            send_mail(subject,body,email,['restaurant@example.com'],fail_silently=False,)
            messages.success(request,"your message has been sent successfully ")
            return redirect('contact')
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form}) 
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
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=FeedbackForm()
        return render(request,'feedback.html'.{'form':form})


def current_year(request):
    return {"current_year":datetime.now().year}

def home1(request):
    menu_items=MenuItem.objects.all()
    address=RestaurantLocation.objects.first()
    return render(request,'index.html',{'menu_items':menu_items,'address':address})

def home_view(request):
    query=request.GET.get('q')
    if query:
        items=MenuItem.objects.filter(name__icontains=query)
    else:
        items=MenuItem.objects.all()
    return render(request.'home.html',{"items":items.'query':query})

def faq_view(request):
    faqs=[
        {"abx":"what is abc"},
    ]
    return render(request,"faq.html",{"faqs":faqs})

def privacy_policy(request):
    return render(request,'privacy_policy.html')