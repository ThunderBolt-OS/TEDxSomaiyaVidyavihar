from django.shortcuts import render

# from django.conf.urls import url
from django.http import response

# Create your views here.

def index (request):
  return render(request, 'home/index.html')

def navbar (request):
  return render(request, "home/navbar.html")

