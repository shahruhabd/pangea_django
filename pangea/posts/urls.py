from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    # path('<int:pk>/', views.post_detail, name='post_detail'),x    
]
