from django.urls import path
from . views import home2

urlpatterns = [
    path('account',views.home2,name='account'),
]