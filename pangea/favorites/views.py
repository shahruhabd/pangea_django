from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from posts.models import Post
from django.contrib import messages


@login_required
def add_to_favorite(request, post_id):
    post = Post.objects.get(id=post_id)
    favorite = Favorite(user=request.user, post=post)
    favorite.save()
    messages.success(request, 'Ваше объявление было успешно добавлено в избранное!')
    return redirect('posts:post_detail', pk=post_id)


@login_required
def favorite_posts(request):
    favorite_posts = Favorite.get_favorite_posts_for_user(request.user)
    return render(request, 'favorites_list.html', {'favorite_posts': favorite_posts})
