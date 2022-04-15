from django.shortcuts import render

# from django.conf.urls import url
from django.http import response

# Create your views here.

def index (request):
  return render(request, 'sponsors/index.html')



