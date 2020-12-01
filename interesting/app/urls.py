from django.conf.urls.static import static
from django.urls import path

from app.views import index, create_post

urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create post'),
]
