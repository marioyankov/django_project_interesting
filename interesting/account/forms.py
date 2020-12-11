from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import UserProfile


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
       class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'profile_img', 'birth_date')
        widgets = {
            'birth_date': forms.SelectDateWidget,
        }
