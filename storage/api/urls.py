from django.urls import path
from api import views


urlpatterns=[
    path('',views.getLocation,name='getLocation'),
    path('addLocation',views.addLocation,name='addLocation'),
    path('getItem',views.getItem,name='getItem'),
    path('addItem',views.addItem,name='addItem'),
    path('deleteLocation/<int:pk>/',views.deleteLocation,name='deleteLocation'),
    path('updateLocation/<int:pk>/',views.updateLocation,name='updateLocation'),
    
]