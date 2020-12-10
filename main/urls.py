from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
    path('history/', history, name='history')
]
