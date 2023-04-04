from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView, AddPostView, EditView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('Blogs/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('Blogs/Edit/<int:pk>', EditView.as_view(), name='edit-blog'),
]