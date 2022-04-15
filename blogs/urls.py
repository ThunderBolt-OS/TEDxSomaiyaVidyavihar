from django.urls import path, include
# from blogs import views 
from .views import BlogsView, BlogsDetailView

app_name = 'blogs'
urlpatterns = [
    # path("", views.blogposts, name='blogposts')
    path("", BlogsView.as_view(), name='blogposts'),
    path("<slug:slug>/", BlogsDetailView.as_view(), name='detail_blogs'),
        
]