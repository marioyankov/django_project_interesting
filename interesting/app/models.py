from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(User):
    username = User.username
    password = User.password
    email = None
    first_name = User.first_name
    last_name = User.last_name
    date_joined = User.date_joined


class Post(models.Model):
    image = models.ImageField(
        upload_to='post'
    )
    description = models.TextField(blank=False)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
