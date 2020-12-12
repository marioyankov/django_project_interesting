from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from account.forms import SignUpForm, UserProfileForm
from account.models import UserProfile


def sign_up_user(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }

        return render(request, 'accounts/sign_up.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.user.groups.add(Group.objects.get(name='UserGroup'))
            profile.save()
            login(request, user)
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'accounts/sign_up.html', context)


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': UserProfileForm(),
            'profile_user': user,
            'profile': user.userprofile,
            'posts': user.userprofile.post_set.all(),
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user profile')

        context = {
            'form': form,
        }

        return render(request, 'accounts/edit_profile.html', context)


def edit_profile(request, pk):
    user = request.user if pk is None else User.objects.get(pk=pk)
    # user = request.user.userprofile
    if request.method == 'GET':
        form = UserProfileForm(instance=user.userprofile)
        context = {
            'user': user,
            'form': form,
        }

        return render(request, 'accounts/edit_profile.html', context)

    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user profile')

        context = {
            'user': user,
            'form': form,
        }

        return render(request, 'accounts/edit_profile.html', context)


def sign_out_user(request):
    logout(request)
    return redirect('index')
