from rest_framework.serializers import ModelSerializer
from .models import Post

# from django.contrib.auth import get_user_model


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author','title','text','slug']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author','title','text','slug']


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author','title','text']


# class UserCreateSerializer(ModelSerializer):
#     class Meta:
#         fields = ("username", "email", "password1", "password2")
#         model = get_user_model()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
