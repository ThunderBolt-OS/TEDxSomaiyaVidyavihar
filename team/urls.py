from django.urls import path
from team import views 

app_name = 'team'
urlpatterns = [
    path("", views.index, name='index'),    
    path("team2020", views.team2020, name='team2020'),
    path("team2019", views.team2019, name='team2019'),    
    path("team2018", views.team2018, name='team2018'),
    path("team2017", views.team2017, name='team2017'),   
]