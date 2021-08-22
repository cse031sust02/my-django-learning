from django.contrib import admin

from .models import Course, Gadget, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'purchase_date', 'student']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
