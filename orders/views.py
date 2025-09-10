from django.shortcuts import render

# Create your views here.
def order_confirmation(request):
    order_number='ORD123456'
    context={
        'order_number':order_number
    }
    return render(request,'order_confirmation.html',context)
    