from django.shortcuts import render


def create_post(request):
    return render(request, 'create_post.html')

