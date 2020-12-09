from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .views import *


def loginPage(request):
    if request.method == 'POST':
        email_address = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email_address, password=password)
        if user:
            login(request, user)
            return redirect('main:home')
        else:
            print('Invalid credentials')
    return render(request, 'authentication/login.html')


def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email_address = request.POST['email']
        password = request.POST['password']
        print(password)
        if not User.objects.filter(username=email_address).exists():
            User.objects.create_user(username=email_address,
                                     first_name=first_name,
                                     last_name=last_name,
                                     password=password)
            return redirect('account:login')
        else:
            print('User already exists')
    return render(request, 'authentication/register.html')
