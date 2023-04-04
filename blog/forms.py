from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
