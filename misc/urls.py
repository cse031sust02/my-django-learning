from django.urls import path

from . import views

urlpatterns = [
    path('serializer_demo/', views.serializer_demo, name='serializer-demo'),
]