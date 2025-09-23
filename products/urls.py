from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from . views import MenuItemsViewSet

router=DefaultRouter()
router.register(r'items',MenuItemsViewSet,basename='menu-items')

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',restaurant_menu,name='restaurant-menu'),
    path('menu/',views.Menu_view,name='menu'),
    path('items-by-category',MenuItemsByCategory.as_view(),name='items-by-category'),
    path("",include(router.urls)),

]