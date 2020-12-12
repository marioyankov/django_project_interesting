from django.urls import path, include

from account.views import sign_up_user, user_profile, sign_out_user, edit_profile

urlpatterns = (
    path('', include('django.contrib.auth.urls')),
    path('signup/', sign_up_user, name='sign up user'),
    path('profile/', user_profile, name='user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('edit_profile/<int:pk>/', edit_profile, name='edit profile'),
    path('signout/', sign_out_user, name='sign out user'),
)
