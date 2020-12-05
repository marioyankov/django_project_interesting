from django.conf.urls.static import static
from django.urls import path

from app.views import index, create_post, post_details_and_comment

urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create post'),
    path('post_details/<int:pk>/', post_details_and_comment, name='post details'),
]
