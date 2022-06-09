from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile.models import UserProfile
from user_profile.serializers import GetProfilesSerializer


class GetProfile(APIView):
    def get(self, request, pk):
        profile = UserProfile.objects.get(user=pk)
        serializer = GetProfilesSerializer(profile)

        return Response(serializer.data)
