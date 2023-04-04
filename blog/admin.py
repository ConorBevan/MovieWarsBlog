from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


admin.site.register(Post)
