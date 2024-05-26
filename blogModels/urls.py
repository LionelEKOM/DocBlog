from django.urls import path
from . import views
from .views import BlogDetailView, BlogIndexView, HomeView

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', HomeView.as_view(title = ""), name='Homepage'),
    path('blog/list/', BlogIndexView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('article/', views.creat, name='createArticle'),
]