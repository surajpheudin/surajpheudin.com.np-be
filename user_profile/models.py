from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField()
    thumbnail = models.CharField(max_length=200)

    facebook_link = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)
    youtube_link = models.CharField(max_length=200)
    youtube_video_link = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username