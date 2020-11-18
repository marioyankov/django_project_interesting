from django.shortcuts import render, redirect

from app.forms.create_post import CreatePostForm


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
