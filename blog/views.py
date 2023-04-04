from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse
from .models import Post
from .forms import CreatePost


# def home(request):
#     return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')

# Lists blogs on the home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


# Shows specfic blog post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'


# Create new posts in the frontend
class AddPostView(CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'add_post.html'


# Edit posts
class EditView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content', 'featured_image']
