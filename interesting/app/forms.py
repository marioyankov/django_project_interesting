from django import forms

from app.models import Post


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ['user']


class CommentForm(forms.Form):
    text = forms.Textarea(
        attrs={
            'class': 'form-control rounded-2',
        }
    )
