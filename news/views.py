from news.models import News
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import News
# Create your views here.
class HomeView(ListView):
    model = News
    template_name = 'home.html'