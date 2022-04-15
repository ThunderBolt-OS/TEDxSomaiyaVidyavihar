from django.urls import path, include
from contactUs import views 

app_name = 'contactUs'
urlpatterns = [
    path("", views.index, name='index'),   
    
]