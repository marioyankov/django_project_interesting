from django.shortcuts import render, redirect

from app.forms import CreatePostForm
from app.models import Post


def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'index.html', context)


def create_post(request):
    if request.method == 'GET':
        context = {
            'form': CreatePostForm(),
        }
        return render(request, 'create_post.html', context)
    else:
        form = CreatePostForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'index.html', context)
