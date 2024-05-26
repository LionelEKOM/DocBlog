from django.urls import path
from . import views
from .views import BlogDetailView, BlogIndexView, BlogPostCreateView, BlogPostDeleteView, HomeView, BlogPostUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', HomeView.as_view(title = ""), name='Homepage'),
    path('blog/list/', BlogIndexView.as_view(), name='blog-list'),
    path('blog/create/', BlogPostCreateView.as_view(), name='create_blog'),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<str:slug>/edit', BlogPostUpdateView.as_view(), name='blog-detail-edit'),
    path('blog/<str:slug>/delete', BlogPostDeleteView.as_view(), name='blog-detail-delete'),
    path('article/', views.creat, name='createArticle'),
]