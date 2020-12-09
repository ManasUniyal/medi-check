from django.shortcuts import render
from .views import *


def loginPage(request):
    return render(request, 'authentication/login.html')

def registerPage(request):
    return render(request, 'authentication/register.html')
