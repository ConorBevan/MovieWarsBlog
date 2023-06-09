from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from datetime import datetime, date


class Post(models.Model):
    """
    Model for blog posts
    """
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
