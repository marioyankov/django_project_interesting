from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from account.forms import SignUpForm
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
            profile.save()
            login(request, user)
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'accounts/sign_up.html', context)


def user_profile(request, pk=None):
    pass


def sign_out_user(request):
    logout(request)
    return redirect('index')
