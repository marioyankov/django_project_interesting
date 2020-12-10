from django.db import models
from account.models import UserProfile

# Create your models here.


class Post(models.Model):
    post_name = models.CharField(max_length=30, blank=False)
    image = models.ImageField(
        upload_to='post'
    )
    description = models.TextField(blank=False)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
