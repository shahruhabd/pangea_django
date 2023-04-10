from django.shortcuts import render, redirect
from .models import Post, Favorite

def add_to_favorite(request, post_id):
    post = Post.objects.get(id=post_id)
    favorite_post = Favorite(user=request.user, post=post)
    favorite_post.save()
    request.session['favorite_post_ids'] = list(Favorite.objects.filter(user=request.user).values_list('post_id', flat=True))
    return redirect('post_detail', post_id=post_id)

def remove_from_favorite(request, post_id):
    favorite_post = Favorite.objects.get(user=request.user, post_id=post_id)
    favorite_post.delete()
    request.session['favorite_post_ids'] = list(Favorite.objects.filter(user=request.user).values_list('post_id', flat=True))
    return redirect('post_detail', post_id=post_id)