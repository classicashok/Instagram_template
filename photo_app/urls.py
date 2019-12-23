from django.contrib import admin
from django.urls import path,include
from .views import index,add,edit,profile,delete,profile_edit,addphoto,search

app_name = 'photo_app'

urlpatterns = [
    
    path('',index, name='index'),
    path('add',add, name='add'),
    path('profile_edit/',profile_edit, name='profile_edit'),
    path('profile/',profile, name='profile'),
    path('delete/<int:id>/', delete, name='delete'),
    path('addphoto/',addphoto, name='addphoto'),
    path('search/', search, name='search'),
]