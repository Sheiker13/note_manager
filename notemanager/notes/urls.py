from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserList, UserDetail, NoteList, NoteDetail

urlpatterns = [
    path('admin/users/', UserList.as_view(), name='user-list'),
    path('admin/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('', include('rest_framework.urls')),
]
