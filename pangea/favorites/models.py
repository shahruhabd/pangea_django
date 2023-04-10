from django.db import models


# from users.models import User
# from templates.models import Post
# Create your models here.


class Favorite(models.Model):
    user = models.ForeignKey('users.User', related_name='favorites', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', related_name='favorites', on_delete=models.CASCADE)
