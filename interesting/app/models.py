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
