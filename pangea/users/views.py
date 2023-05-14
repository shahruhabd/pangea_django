from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from posts.models import Post

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

def index(request):
    return render(request, 'users/profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Приветствуем на нашем сайте по поиску руммейтов! Мы поможем вам найти подходящего соседа для совместного проживания. Начните свой поиск прямо сейчас!')
            username = request.POST['username']
            password = request.POST['password']
            remember_me = request.POST.get('remember_me')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)
                return HttpResponseRedirect(reverse('posts:post_list'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    user = request.user
    my_posts = Post.objects.filter(user_id=user, archived=False).order_by('-created_at')
    archived_posts_count = Post.objects.filter(user_id=user, archived=True).count()
    context = {
        'user': user,
        'my_posts': my_posts,
        'archived_posts_count': archived_posts_count,
        'title': 'Профиль', 
        'form': form
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))
