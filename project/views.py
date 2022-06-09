from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import Project
from project.serializers import GetProjectsSerializer


class GetProjects(APIView):
    def get(self, request, pk):
        page_number = request.query_params.get('page_number', 1)
        page_size = request.query_params.get('page_size', 10)

        projects = Project.objects.filter(user=pk).order_by('-created_at')

        paginator = Paginator(projects, page_size)

        serializer = GetProjectsSerializer(paginator.page(page_number), many=True)

        return Response(serializer.data)
