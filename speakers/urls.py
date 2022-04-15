from django.urls import path, include
from speakers import views 

app_name = 'speakers'
urlpatterns = [
    path("", views.index, name='index'),    
    path("speakers2021", views.speakers2021, name='speakers2021'),    
    path("speakers2020", views.speakers2020, name='speakers2020'),    
    path("speakers2019", views.speakers2019, name='speakers2019'),    
    path("speakers2018", views.speakers2018, name='speakers2018'),    
    path("speakers2017", views.speakers2017, name='speakers2017'),    
]