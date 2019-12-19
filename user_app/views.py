from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserModel
# Create your views here.
def index(request):
    return render(request, 'index.htm')

def display(request):
    return render(request, 'display.htm')
    
def login(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('pass')

        user = UserModel.objects.filter(email=e,password=p)

        if(user.count()>0):
            for user in user:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['username'] = user.username
                return redirect('photo_app:index')


        else: 
            return HttpResponse("Wrong Credintials")

    else:
        return render(request, 'login.htm')

def logout(request):
    request.session.flush()
    return redirect('user:login')
