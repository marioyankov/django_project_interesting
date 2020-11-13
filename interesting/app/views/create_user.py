from django.shortcuts import render

from app.forms.create_profile import CreateProfileForm


def create_user(request):
    context = {
        'form': CreateProfileForm(),
    }
    return render(request, 'create_user.html', context)
