from django.contrib.auth.models import User
from django.db import models


# Create your models here.

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
