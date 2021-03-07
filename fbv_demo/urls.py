from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:article_id>/', views.article_details, name='article-detail'),
]
