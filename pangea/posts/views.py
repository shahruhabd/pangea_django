from django.core.files.storage import default_storage
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Post
from rent.models import Rent
from .forms import PostDeleteForm, PostForm
from django.contrib import messages


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
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
    return render(request, 'posts/post_detail.html', {'post': post})


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

