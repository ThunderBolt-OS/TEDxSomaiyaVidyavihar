from django.shortcuts import render

# from django.conf.urls import url
from django.http import response

# Create your views here.

def index (request):
  return render(request, 'home/index.html')

def navbar (request):
  return render(request, "home/navbar.html")

def error_404_view (request, exception):
  return render(request, "home/404.html")

def error_500_view (request):
  return render(request, "home/500.html")

