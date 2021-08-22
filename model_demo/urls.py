from django.urls import path

from . import views

urlpatterns = [
    path('students/<int:student_id>/', views.student_demo, name='student-demo'),
]
