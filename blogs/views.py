from django.shortcuts import render

from django.http import response
from django.views.generic import ListView, DetailView
from .models import Post



class BlogsView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_at')
  template_name = 'blogs/blogs.html'

class BlogsDetailView(DetailView):
  model = Post
  template_name = 'blogs/blogs_detailview.html'
