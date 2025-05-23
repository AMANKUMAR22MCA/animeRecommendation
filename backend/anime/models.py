from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    favorite_genres = models.TextField(blank=True, null=True)
    watched_anime = models.JSONField(default=list)
