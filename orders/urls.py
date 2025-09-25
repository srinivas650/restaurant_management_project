from django.urls import path
from .views import *

urlpatterns = [
    path('order',views.order_confirmation,name='orderconfirmation'),
    path('history',OrderHistoryView.as_view(),name='order-history'),
    path('<int:id>/',orderDetailView.as_view(),name='order-detail'),
]