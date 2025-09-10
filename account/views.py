from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

def home2(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=authenticate(request,username=username,password=password)
        if user in not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')
    return render(request,'account.html')
