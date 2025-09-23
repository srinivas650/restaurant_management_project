from django.urls import path
from . import views

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',restaurant_menu,name='restaurant-menu'),
    path('menu/',views.Menu_view,name='menu'),
    path('items-by-category',MenuItemsByCategory.as_view(),name='items-by-category'),
]