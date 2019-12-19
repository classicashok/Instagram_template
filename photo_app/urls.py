from django.contrib import admin
from django.urls import path,include
from .views import index,add,edit

app_name = 'photo_app'

urlpatterns = [
    
    path('',index, name='index'),
    path('add',add, name='add'),
    path('edit/<int:id>/',edit, name='edit'),
    
]