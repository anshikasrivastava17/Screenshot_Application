from django.shortcuts import render,  redirect
import random
import pyautogui
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model

def index(request):
    if request.method == "POST":
        ss = pyautogui.screenshot()
        img = f'myimg{random.randint(1000,9999)}.png'
        ss.save(settings.MEDIA_ROOT/img)
        messages.success(request,'screenshot has been taken')
        return render(request,'index.html',{'img':img})
    return render(request,'index.html')

