
from django.shortcuts import render

# Create your views here.

def index (request):
  return render(request, 'team/index.html')

def team2020 (request):
  return render(request, 'team/team2020.html')

def team2019 (request):
  return render(request, 'team/team2019.html')

def team2018 (request):
  return render(request, 'team/team2018.html')

def team2017 (request):
  return render(request, 'team/team2017.html')





