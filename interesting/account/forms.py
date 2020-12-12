from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.FormControlMixin import FormControlMixin
from account.models import UserProfile


class SignUpForm(FormControlMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


class UserProfileForm(FormControlMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'profile_img', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput,
        }
