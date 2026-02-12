from .models import Blog, Comment

from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model= Blog
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"