from django.contrib import admin
from django.urls import path, include
from posts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page, name='start-page'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
<<<<<<< HEAD
    path('favorites/', include('favorites.urls', namespace='favorites')),
=======
    path('chat/', include('chat.urls', namespace='chat')),
>>>>>>> 7f86958def60edf3879649233fae4fbb48eb1bd2
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
