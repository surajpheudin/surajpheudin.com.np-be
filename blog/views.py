from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog
from blog.serializers import GetBlogsSerializer


class GetBlogs(APIView):
    def get(self, request, pk):
        page_number = request.query_params.get('page_number', 1)
        page_size = request.query_params.get('page_size', 10)

        blogs = Blog.objects.filter(user=pk).order_by('-created_at')

        paginator = Paginator(blogs, page_size)

        serializer = GetBlogsSerializer(paginator.page(page_number), many=True)

        return Response(serializer.data)
