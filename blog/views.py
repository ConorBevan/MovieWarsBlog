from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from .forms import CreatePost
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    paginate_by = 6


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


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
