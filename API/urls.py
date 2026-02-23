from django.urls import path
from .views import GetAllArticles, GetArticle

urlpatterns = [
    path('articles/', GetAllArticles.as_view(), name='get_articles'),
    path('article/<int:pk>/', GetArticle.as_view(), name='get_article'),
]