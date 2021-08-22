from django.db import models
from django.utils import timezone

"""
One to Many : Student -> Gadget
Many to Many : Student <-> Course
"""


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    # courses = models.ManyToManyField(
    #     Course, through=a, related_name="courses")

    def __str__(self):
        return self.name


class Gadget(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField('date purchased')

    def __str__(self):
        return self.title

    def was_purchased_recently(self):
        return self.purchase_date >= timezone.now() - datetime.timedelta(days=1)
