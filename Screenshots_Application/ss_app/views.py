from django.shortcuts import render,  redirect
import random
import os
import time
import pyautogui
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.shortcuts import render
import fun


def index(request):
    if request.method == "POST":
        time.sleep(5)
        ss = pyautogui.screenshot()
        name=str(request.user.username)
        img_path=fun.namingfile(ss, name)
        messages.success(request,'screenshot has been taken')
        return render(request,'index.html',{'img_path': img_path})
    return render(request,'index.html')

def home(request):
    return render (request, "home.html")

def signup(request):
    if not request.user.is_anonymous: #works when user is logged in 
        return redirect("/dashboard") 
    if request.method=="POST":

        User = get_user_model()
        users = User.objects.all()
        user_list=[]
        email_list=[]
        for i in users:
            user_list.append(i.username)
            email_list.append(i.email)

        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if email in email_list:
            messages.error(request, 'Email already signed up. Head to login page.')
            return render(request,'signup.html')
        
        if name in user_list:
            messages.error(request, 'Username already Taken. Please try something else.')
            return render(request,'signup.html')
        
        user = User.objects.create_user(username=name, email=email, first_name=name, password=password)
        user.save()
        messages.success(request, f'Your account is created {name}. Head to login page!')

        npath = os.path.join(settings.MEDIA_ROOT, name)
        os.mkdir(npath)
        
    return render(request,'signup.html')

def signin(request):
    if not request.user.is_anonymous:
            return redirect('/dashboard')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request,'signin.html')
    return render(request,'signin.html')

def logoutuser(request):
    logout(request)
    return redirect('/signin')

def edit(request):
     img_path=request.GET.get('img_path')
     if not fun.premium(str(request.user.username)):
         return redirect('/upgrade')
     return render(request,'edit.html', {"img_path":img_path})

def upgrade(request):
    return render(request,"upgrade.html")

def addpremium(request):
    name = (str(request.user.username))
    fun.addtopremium(name)
    return redirect("/dashboard")

def dashboard(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    
    name=request.user.username
    ss_list=fun.ss_list(name)

    dic={'ss_list':ss_list,'name':name}
    return render(request,'dashboard.html',dic)

def screenshot(request):
    if request.user.is_anonymous:
        return redirect("/sigin")
    
    ss = request.GET.get('ss')  
    name = request.user.username
    path = f"{name}/{ss}"

    return render(request, 'screenshot.html', {"path":path})