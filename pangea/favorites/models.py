from django.db import models
# from users.models import User
# from posts.models import Post
# Create your models here.

class Favorite(models.Model):

    user = models.ForeignKey('users.User', related_name='favorites',on_delete=models.RESTRICT)
    post = models.ForeignKey('posts.Post', related_name='favorites',on_delete=models.RESTRICT)