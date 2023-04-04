from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse
from .models import Post
from .forms import CreatePost


# def home(request):
#     return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'add_post.html'


class EditView(UpdateView):
    model = Post
    form_class = CreatePost
    template_name = 'update_post.html'
