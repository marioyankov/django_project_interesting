from django import forms

from app.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
