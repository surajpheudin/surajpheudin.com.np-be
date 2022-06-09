from rest_framework import serializers

from blog.models import Blog


class GetBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['user']
