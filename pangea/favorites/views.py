from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from posts.models import Post

@login_required
def add_to_favorite(request, post_id):
    post = Post.objects.get(id=post_id)
    favorite = Favorite(user=request.user, post=post)
    favorite.save()
    return redirect('post_detail', post_id=post_id)

@login_required
def favorite_posts(request):
    favorite_posts = Favorite.get_favorite_posts_for_user(request.user)
    return render(request, 'favorite_posts.html', {'favorite_posts': favorite_posts})
