from django.conf.urls.static import static
from django.urls import path

from app.views.create_post import create_post
from app.views.create_user import create_user
from app.views.index import index
from interesting import settings

urlpatterns = [
    # index
    path('', index, name='index'),
    # users
    path('create_post/', create_post, name='create post'),
    path('create_user/', create_user, name='create user'),
    # posting
    path('create_post/', create_post, name='create post'),
]
