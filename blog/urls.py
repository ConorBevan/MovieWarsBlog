from django.urls import path
from .views import HomeView, BlogDetailView, AddPostView, EditView, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Blogs/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('Blogs/Edit/<int:pk>', EditView.as_view(), name='edit-blog'),
    path('Blogs/<int:pk>/delete', DeletePost.as_view(), name='delete-blog'),
]
