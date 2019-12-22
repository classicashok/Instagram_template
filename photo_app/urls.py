from django.contrib import admin
from django.urls import path,include
from .views import index,add,edit,profile,delete

app_name = 'photo_app'

urlpatterns = [
    
    path('',index, name='index'),
    path('add',add, name='add'),
    path('edit/<int:id>/',edit, name='edit'),
    path('profile/',profile, name='profile'),
    path('delete/<int:id>/', delete, name='delete')
]