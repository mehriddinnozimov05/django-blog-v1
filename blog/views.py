from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
# Create your views here.
class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog_create.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog_delete.html"
    success_url = reverse_lazy('blog')