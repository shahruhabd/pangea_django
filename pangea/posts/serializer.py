from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at', 'updated_at', 'cost', 'user_id']
