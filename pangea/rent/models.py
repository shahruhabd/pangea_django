from django.db import models
from users.models import User
from posts.models import Post

class Rent(models.Model):
    is_rent = models.BooleanField(default=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.post_id} - {self.user_id} - {self.is_rent}'

