from django.db import models
from users.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.CharField(null=False, max_length=2000)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


