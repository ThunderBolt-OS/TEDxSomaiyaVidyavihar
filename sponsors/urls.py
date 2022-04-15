from django.urls import path, include
from sponsors import views 

app_name = 'sponsors'
urlpatterns = [
    path("", views.index, name='index'),    
]