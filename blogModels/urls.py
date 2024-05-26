from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', HomeView.as_view(title = "Page d'acceuil"), name='Homepage'),
    path('article/', views.creat, name='createArticle'),
]