from rest_framework import serializers

from Blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        field = '__all__'
