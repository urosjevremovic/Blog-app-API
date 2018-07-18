from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created')
        model = Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username')
        model = get_user_model()