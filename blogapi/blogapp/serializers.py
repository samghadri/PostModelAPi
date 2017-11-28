from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.TextField()
    created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
