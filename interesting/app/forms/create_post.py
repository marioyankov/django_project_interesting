from django_project_interesting.interesting.app.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
