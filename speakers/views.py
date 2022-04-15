from django.shortcuts import render

# from django.conf.urls import url
from django.http import response

# Create your views here.

def index (request):
  return render(request, 'speakers/index.html')

def speakers2017 (request):
  return render(request, 'speakers/speakers2017.html')

def speakers2018 (request):
  return render(request, 'speakers/speakers2018.html')

def speakers2019 (request):
  return render(request, 'speakers/speakers2019.html')

def speakers2020 (request):
  return render(request, 'speakers/shots1.html')

def speakers2021 (request):
  return render(request, 'speakers/shots2.html')





