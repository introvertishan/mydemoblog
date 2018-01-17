from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import *
from .forms import *
from .models import *
# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return redirect('blog:index')
def invalid(request):
    error = "a"
    return render(request, 'login.html', {'error': error})

def home(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)
def signup(request):
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            img = request.FILES['profile_pic']
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #confirmpassword = form.cleaned_data['confirmpassword']
            #pic = request.POST.get("profile_pic")
            a = User.objects.create_user(username=username,password=password,email=email)
            a
            obj = userinfo(user=a,firstname=firstname,lastname=lastname,profile_pic=img)
            obj.save()
            return redirect('loginapp:home')
        else:
            err = form.errors
            #print(', '.join("%s: %s" % item for item in err()))
            return render(request, 'register.html', {'err': err})
    else:
        form=regform()
        return render(request,'register.html')
    return render(request, 'register.html')

def auth_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('loginapp:home')
    else:
        return redirect('loginapp:invalid')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')