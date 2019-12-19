from django.contrib import admin
from django.urls import path,include

from user_app.views import index,display,login,logout

app_name ='user'
urlpatterns = [

      path('',index),
      path('display/',display, name='display'),
      path('login/',login, name='login'),
      path('logout/',logout, name='logout')
    
   ]