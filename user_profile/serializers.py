from rest_framework import serializers

from user_profile.models import UserProfile


class GetProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['user']
