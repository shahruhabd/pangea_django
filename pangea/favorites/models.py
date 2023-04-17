from django.db import models
from posts.models import Post
from django.conf import settings

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_favorite_posts_for_user(user):
        return Favorite.objects.filter(user=user).order_by('-created_at')
