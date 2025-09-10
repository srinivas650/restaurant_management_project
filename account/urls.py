from django.urls import path
from .views import account

urlpatterns = [
    path('account',views.home2,name='account'),
]