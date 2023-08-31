from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    is_blocked = models.BooleanField(default=False)


class Post(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    text = models.CharField(max_length=80, null=False, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    is_published = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
