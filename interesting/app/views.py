import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from app.forms import CreatePostForm, CommentForm
from app.models import Post, Comment, Like


class IndexListView(ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = 2


def create_or_edit_post(request, post, template):
    if request.method == 'GET':
        form = CreatePostForm(instance=post)

        context = {
            'form': form,
            'post': post,
        }

        return render(request, f'{template}.html', context)

    else:
        old_image = post.image
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if old_image:
                os.remove(old_image.path)
            post = form.save(commit=False)
            post.user = request.user.userprofile
            post.save()
            return redirect('post details', post.pk)

        context = {
            'form': form,
            'post': post,
        }

        return render(request, f'{template}.html', context)


@login_required
def create_post(request):
    post = Post()
    return create_or_edit_post(request, post, 'create_post')


@login_required
def post_details_and_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        post.likes_count = post.like_set.count()
        context = {
            'post': post,
            'form': CommentForm(),
            'can_delete': request.user == post.user.user or request.user.is_staff,
            'can_edit': request.user == post.user.user or request.user.is_staff,
            'can_like': request.user != post.user.user,
            'has_liked': post.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != post.user.user or request.user.is_staff,
        }

        return render(request, 'post_details.html', context)
    else:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'], )
            comment.post = post
            comment.user = request.user.userprofile
            comment.save()
            return redirect('post details', pk)

        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'post_details.html', context)


@login_required
def like_post(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, post_id=pk).first()
    if like:
        like.delete()
    else:
        post = Post.objects.get(pk=pk)
        like = Like(user=request.user.userprofile)
        like.post = post
        like.save()
    return redirect('post details', pk)


#
# @login_required
# def edit_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     return create_or_edit_post(request, post, 'post_edit')

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreatePostForm(instance=post)

        context = {
            'form': form,
            'post': post,
        }

        return render(request, 'post_edit.html', context)

    else:
        old_image = post.image
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if old_image:
                os.remove(old_image.path)
            post = form.save(commit=False)
            post.save()
            return redirect('post details', post.pk)

        context = {
            'form': form,
            'post': post,
        }

        return render(request, 'post_details.html', context)


@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'post': post,
        }

        return render(request, 'post_delete.html', context)

    else:
        post.delete()
        return redirect('index')
