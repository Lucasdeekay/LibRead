from rest_framework import viewsets

from Blog.models import Blog, Comment
from Blog.serializers import BlogSerializer, CommentSerializer


class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
