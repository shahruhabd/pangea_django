from django.db import models
from users.models import User
# from django.urls import reverse


class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.CharField(null=False, max_length=2000)
    image = models.ImageField(upload_to='post_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(null=False)
    user_id = models.ForeignKey(User, null=False, on_delete=models.RESTRICT)

    # def get_absolute_url(self):
    #     return reverse('post',kwargs={'post_id':self.pk})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
