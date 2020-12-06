from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms import CreatePostForm, CommentForm
from app.models import Post, Comment, Like


def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'index.html', context)


@login_required
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


@login_required
def post_details_and_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        post.likes_count = post.like_set.count()
        context = {
            'post': post,
            'form': CommentForm(),
            'can_delete': request.user == post.user.user,
            'can_edit': request.user == post.user.user,
            'can_like': request.user != post.user.user,
            'has_liked': post.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != post.user.user,
        }

        return render(request, 'post_details.html', context)
    else:
        form = CommentForm(request.POST, request.FILES)

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
        like = Like(post=request.post, user=request.user.userprofile)
        like.post = post
        like.save()
    return redirect('post details', pk)


@login_required
def delete_post(request, pk):
    pass
