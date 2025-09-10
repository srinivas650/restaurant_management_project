from django.urls import path
from .views import *

urlpatterns = [
    path('account',views.home2,name='account'),
]