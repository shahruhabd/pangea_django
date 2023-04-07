from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'posts/post_add.html', {'form': form})


def page(request):
    return render(request, 'posts/start-page.html')
