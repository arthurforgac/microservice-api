from django.urls import path, include
from .views import PostViewSet, UserViewSet


urlpatterns = [
    path('posts', PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
        })),
    path('posts/<str:pk>', PostViewSet.as_view({
        'get': 'retrieve_by_id',
        'put': 'update',
        'delete': 'destroy',
        })),
    path('user/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve_by_userid'
    }))
]
