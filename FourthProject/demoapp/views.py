from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python_view(request):
    return HttpResponse("<h1>Welcome to python world</h1>")

def django_view(request):
    return HttpResponse("<h1>Welcome to Django world</h1>")

def restAPI_view(request):
    return HttpResponse("<h1>Welcome to restAPI world</h1>")      
