from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    first_name = models.CharField
    last_name = models.CharField
    birth_date = models.DateTimeField

    def __str__(self):
        return self.user.username
