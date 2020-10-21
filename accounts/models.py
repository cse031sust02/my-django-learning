from django.db import models
from django.contrib.auth.models import AbstractUser

class BloggerUser(AbstractUser):
    website = models.CharField(max_length=200)
