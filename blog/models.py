from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    post_date = models.DateField(auto_now_add=True)

    def num_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
