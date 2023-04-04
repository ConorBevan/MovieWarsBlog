from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView

urlpatterns = [
    # path('', views.home, name='home'),
    # path('about/', views.about, name='blog-about'),
    path('', HomeView.as_view(), name="home"),
    path('Blogs/<int:pk>', BlogDetailView.as_view(), name="blog-detail"),
]
