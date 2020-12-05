from django.urls import path, include

from account.views import sign_up_user, user_profile, sign_out_user

urlpatterns = (
    path('', include('django.contrib.auth.urls')),
    path('signup/', sign_up_user, name='sign up user'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signout/', sign_out_user, name='sign out user'),
)
