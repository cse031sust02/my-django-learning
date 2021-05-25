from django.urls import path

from . import views

urlpatterns = [
    path('demo/', views.model_demo, name='model-demo'),
]
