from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from posts.models import Post
from posts.permissions import IsAuthorOrAdminOrReadOnly
from posts.serializers import PostSerializer, UserSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrAdminOrReadOnly, )


class UserList(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer