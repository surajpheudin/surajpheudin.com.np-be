from rest_framework import serializers

from project.models import Project


class GetProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['user']
