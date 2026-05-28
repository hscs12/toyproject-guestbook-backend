from django.urls import path
from .views import PostListCreateView, PostDeleteView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDeleteView.as_view()),
]