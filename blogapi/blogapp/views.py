from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    UpdateAPIView, DestroyAPIView, CreateAPIView)
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer

class PostApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateApi(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostCreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
