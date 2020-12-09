from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home(request):
    return render(request, 'main/homepage.html')


@require_http_methods(["POST"])
def result(request):
    print('Hello')
    return render(request, 'main/result.html')
