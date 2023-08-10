from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from .forms import CreatePost
from django.urls import reverse_lazy
from django.contrib import messages


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

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Post created successfully!')
        return response


class EditView(UpdateView):
    model = Post
    form_class = CreatePost
    template_name = 'update_post.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Post edited successfully!')
        return response


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Post deleted successfully!')
        return response
