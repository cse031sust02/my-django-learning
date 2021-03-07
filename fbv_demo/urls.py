from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.artcile_list, name='article-list')
]
