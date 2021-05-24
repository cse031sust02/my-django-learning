from django.urls import path

from . import views

urlpatterns = [
    path('demo/', views.file_upload_demo, name='file-upload-demo'),
]
