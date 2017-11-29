from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostSerializer

class PostApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
