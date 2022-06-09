from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    body = models.TextField()
    thumbnail = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title