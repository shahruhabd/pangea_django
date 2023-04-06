from django.contrib import admin
from django.urls import path, include
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page, name='start-page'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
]
