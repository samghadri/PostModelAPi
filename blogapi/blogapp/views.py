from rest_framework.generics import ListAPIView
from .models import Post

class PostApi(ListAPIView):
    queryset = Post.objects.all()

    
