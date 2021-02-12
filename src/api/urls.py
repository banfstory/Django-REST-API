from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('forums/', include('forums.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('replys/', include('replys.urls')),
]