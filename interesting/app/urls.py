from django.urls import path

from app.views.create import create_post
from app.views.index import index

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_post, name='create post')
]
