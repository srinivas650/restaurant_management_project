from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq_view,name="faq"),
    path('api/restaurant/'RestaurantListAPIView.as_view(),name='restaurant-list'),
    path('api/tables/',TableListAPIView.as_view(),name='table-list'),
    path('api/tables/<int:pk>/',TableDetailAPIView.as_view(),name='table-detail'),
]