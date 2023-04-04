from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post


# def home(request):
#     return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
