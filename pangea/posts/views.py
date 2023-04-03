from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                title = form.data.get('title')
                description = form.data.get('description')
                cost = form.data.get('cost')
                post = Post(title=title, description=description, cost=cost, user_id_id=request.user.id)
                post.save()
                return redirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
