from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer

class PostApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
