from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def restaurant_menu(request):
    menu=[
        {
            'name':'panner butter masala',
            'description':'butter based curry with panner(sweet)',
            'price':250
        }
        {
            'name':'chicken Biryani',
            'description':'rice cooked with chicken and spices',
            'price':'300'
        }

    ]
    return response(menu)
def menu_view(request):
    items=Item.objects.filter(is_available=True)
    return render(request,'menu.html',{'menu_items':items})

def hom_view(request):
    cart_count=0
    if request.user.is_authenticated:
        cart_count=CartItem.objects.filter(user=request.user).aggregate(total=models.Sum('quantity'))['total']or 0
    return render(request,'menu.item',{'cart_count':cart_count})


    class MenuItemByCategory(APIView):
        def get(self,request):
            category=request.query_params.get("category")

            if not category:
                return Response({"error":"category paramter is required."},status=status.HTTP_400_BAD_REQUEST)
            items=MenuItems.objects.filter(category__name__iex,act=category)
            serializer=MenuItemSerializer(items,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset=MenuItems.objects.all()
    serializer_class=MenuItemsSerializer
    permission_classes=[IsAdminUser]

    def update(self,request,*args,**kwargs):
        try:
            return super().update(request,*args,**kwargs)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class MenuItemsSearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=MenuItems.objects.all()
    serializer_class=MenuItemSerializer
    pagination_class=MenuItemsPagination

    def list(self,request,*args,**kwargs):
        search_query=request.query_params.get("search",None)
        if search_query:
            self.queryset=self.queryset.filter(name__icontains=search_query)
        page=self.paginate_queryset(self.queryset)
        if page is not None:
            serializer=self.get_serializer(page,many=True)
            return  self.get_paginated_response(serializer.data)
        serializer=self.get_serializer(self.queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)