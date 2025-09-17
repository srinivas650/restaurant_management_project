from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq_view,name="faq"),
    path('api/restaurant/'RestaurantListAPIView.as_view(),name='restaurant-list'),
]