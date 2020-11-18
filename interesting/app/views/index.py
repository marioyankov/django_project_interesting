from django.shortcuts import render

from app.forms.create_post import CreatePostForm
from app.models import Post


def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'index.html', context)
