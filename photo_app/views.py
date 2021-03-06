from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PhotoModel
from .forms import PhotoForm
from .models import UserModel

# Create your views here.
def index(request):
    if 'id' in request.session:
        upload = PhotoModel.objects.all()[:20]
        return render(request, 'photo_app/index.htm',{'upload':upload})
    else:
        return redirect('user:login')

def edit(request,id):
    photo = PhotoModel.objects.get(id=id)
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not valid')

    else:
        # form = PhotoForm
        return render(request,"photo_app/editphoto.htm",{'photo:':photo})

def add(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not valid')

    else:
        form = PhotoForm
        return render(request,"photo_app/addphoto.htm",{'form:':form})


def profile(request):
    if 'id' in request.session:
        user_id = request.session['id']
        upload = PhotoModel.objects.filter(uploaded_by=user_id)
        user = UserModel.objects.get(id= user_id)
        dict = {'upload':upload,'user':user}
        return render(request, 'photo_app/profile.htm',dict)
    else:
        return redirect('user:login')

def delete(request,id)  :
    photo = PhotoModel.objects.get(id=id)   
    photo.delete()
    return redirect('photo_app:profile')   

def profile_edit(request):
    if 'id' in request.session:
        user_id = request.session['id']
        upload = PhotoModel.objects.filter(uploaded_by=user_id)
        user = UserModel.objects.get(id= user_id)
        dict = {'upload':upload,'user':user}
        return render(request, 'photo_app/edit-profile.htm',dict)
    else:
        return redirect('user:login')

def addphoto(request) :
    if 'id' in request.session:
        user_id = request.session['id']
        upload = PhotoModel.objects.filter(uploaded_by=user_id)
        user = UserModel.objects.get(id= user_id)
        dict = {'upload':upload,'user':user}
        return render(request,'photo_app/addphoto.htm',dict) 
    else:
        return redirect('user:login')


def search(request):
    if 'id' not in request.session:
        return redirect('user:login')

    user_id = request.session.get('q',None)

    if request.method == 'GET':
        querry = request.GET.get('q',None)
        if querry:
            d = {
                'profiles':UserModel.objects.filter(username__icontains=querry).exclude(id=user_id),
                'querry':querry
            }
            return render(request,'photo_app/search_results.htm', d)
        else:
            return redirect('photo_app:index')
    else:
        return redirect('photo_app:index')