from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import Order
from . serializers import OrderSerializer
from rest_framework import generics

# Create your views here.
def order_confirmation(request):
    order_number='ORD123456'
    context={
        'order_number':order_number
    }
    return render(request,'order_confirmation.html',context)
    
class OrderHistoryView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        orders=Order.objects.filter(user=request.user).order_by('-order_date')
        serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)
class OrderDetailView(generics.RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    lookup_field="id"


