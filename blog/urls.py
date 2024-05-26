from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('signup/', views.signup, name='signup'),
    path('article-<str:numero_article>/', views.article, name='blog-article'),
]
