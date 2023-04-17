from django.core.files.storage import default_storage
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            image = request.FILES.get('image')
            cost = request.POST.get('cost')
            post = Post(title=title, description=description, image=image, cost=cost, user_id=request.user)
            # post = form.save()
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


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/posts/')
    context = {'post': post}
    return render(request, 'post_delete.html', context)
