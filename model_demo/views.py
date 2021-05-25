from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def model_demo(request):
    context = {}
    return render(request, 'file_demo/index.html', context)
