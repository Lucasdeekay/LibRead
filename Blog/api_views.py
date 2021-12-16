from rest_framework import viewsets

from Blog.models import Blog
from Blog.serializers import BlogSerializer


class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
