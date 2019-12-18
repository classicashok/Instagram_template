from django.shortcuts import render
from django.http import HttpResponse
from .models import PhotoModel
# Create your views here.
def index(request):
    upload = PhotoModel.objects.all()
    return render(request, 'photo_app/index.htm',{'upload':upload})
