from django.urls import path
from .views import add_to_favorite, favorite_posts

app_name = 'favorites'

urlpatterns = [
    path('posts/<int:post_id>/favorite/', add_to_favorite, name='add_to_favorite'),
    path('', favorite_posts, name='favorite_posts'),
]
