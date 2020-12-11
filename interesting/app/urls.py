from django.urls import path

from app.views import create_post, post_details_and_comment, edit_post, delete_post, like_post, IndexListView

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexListView.as_view(), name='index'),
    path('create_post/', create_post, name='create post'),
    path('post_details/<int:pk>/', post_details_and_comment, name='post details'),
    path('edit/<int:pk>', edit_post, name='edit post'),
    path('like/<int:pk>', like_post, name='like post'),
    path('delete/<int:pk>', delete_post, name='delete post'),
]
