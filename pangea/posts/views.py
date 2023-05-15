from datetime import timezone
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Post, Favorite
from rent.models import Rent
from .forms import PostDeleteForm, PostForm
from django.contrib import messages


def post_list(request):
    user = request.user
    posts = Post.objects.filter(archived=False).order_by('-created_at')
    posts_count = Post.objects.filter(archived=False).count()
    archive_count = Post.objects.filter(user_id=user, archived=True).count()
    favorite_count = Favorite.objects.filter(user=user).count()
    favorites = Favorite.objects.filter(user=request.user, post__in=posts)
    favorite_posts = favorites.values_list('post', flat=True)
    return render(request, 'posts/post_list.html', {'posts': posts, 'favorite_posts': favorite_posts, 'posts_count': posts_count, 'archive_count': archive_count, 'favorite_count': favorite_count })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            messages.success(request, 'Ваше объявление было успешно опубликовано!')
            post.save()
            return redirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'posts/post_add.html', {'form': form})

def page(request):
    return render(request, 'posts/start-page.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, post=post).exists()
    return render(request, 'posts/post_detail.html', {'post': post, 'is_favorite': is_favorite})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostDeleteForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            is_rent = form.cleaned_data['is_rent']
            rent = Rent.objects.create(user_id=request.user, post_id=post, is_rent=is_rent)
            rent.save()
            post.delete()
            return redirect('posts:post_list')
    
    return render(request, 'posts/post_delete.html', {'post': post})


def archive_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.archived = True
    messages.success(request, 'Ваше объявление было успешно добавлено в архив!')
    post.save()
    return redirect('posts:post_list')

def return_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.archived = False
    messages.success(request, 'Ваше объявление было успешно опубликовано!')
    post.save()
    return redirect('posts:post_list')

def archive_list(request):
    user = request.user
    posts = Post.objects.filter(user_id=user, archived=True).order_by('-created_at')
    posts_count = Post.objects.filter(archived=False).count()
    archive_count = Post.objects.filter(user_id=user, archived=True).count()
    favorite_count = Favorite.objects.filter(user=user).count()
    return render(request, 'posts/archive_list.html', {'posts': posts, 'posts_count': posts_count, 'archive_count': archive_count, 'favorite_count': favorite_count})

def favorite_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)
    messages.success(request, 'Ваше объявление было успешно добавлено в избранное!')
    return redirect('posts:post_list')

def remove_favorite_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Favorite.objects.filter(user=request.user, post=post).delete()
    messages.success(request, 'Ваше объявление было успешно удалено из избранного!')
    return redirect('posts:post_list')

def favorite_list(request):
    user = request.user
    favorites = Favorite.objects.filter(user=request.user).order_by('-created_at')
    posts_count = Post.objects.filter(archived=False).count()
    archive_count = Post.objects.filter(user_id=user, archived=True).count()
    favorite_count = Favorite.objects.filter(user=user).count()
    return render(request, 'posts/favorite_list.html', {'favorites': favorites, 'posts_count': posts_count, 'archive_count': archive_count, 'favorite_count': favorite_count})

