from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Student


def student_demo(request, student_id):
    student = Student.objects.get(id=student_id)
    student_gadgets = student.gadget_set.all()
    context = {
        'student': student,
        'student_gadgets': student_gadgets
    }
    return render(request, 'model_demo/student.html', context)
