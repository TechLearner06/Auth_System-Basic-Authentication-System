from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request,'Home.html')


def Login(request):
    if request.method == 'POST':
        username=request.POST['user_name']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exist')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.info(request,'registered successfully')
        else:
            messages.info(request,'password didnot match')
        return redirect('register')
    else:
        return render(request,'register.html')
    

def Logout(request):
    logout(request)
    return redirect('/')


