from django.urls import path, include
from home import views 

app_name = 'home'
urlpatterns = [
    path("", views.index, name='index'),    
    path("navbar", views.navbar, name='navbar'),
]