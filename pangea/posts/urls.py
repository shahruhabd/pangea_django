from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    # Посты
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),

    # Архив
    path('archive/', views.archive_list, name='archive_list'),
    path('<int:pk>/archive/', views.archive_post, name='archive_post'),
    path('return_post/<int:pk>/', views.return_post, name='return_post'),

    # Избранное
    path('favorite/', views.favorite_list, name='favorite_list'),
    path('<int:pk>/favorite/', views.favorite_post, name='favorite_post'),
    path('remove_favorite/<int:pk>/', views.remove_favorite_post, name='remove_favorite_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
