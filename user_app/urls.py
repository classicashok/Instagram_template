from django.contrib import admin
from django.urls import path,include

from user_app.views import index,display

urlpatterns = [

      path('',index),
      path('display/',display)
    
   ]