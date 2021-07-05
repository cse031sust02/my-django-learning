from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .forms import UploadFileForm


def file_upload_demo(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'file_demo/index.html', context)
    elif request.method == 'POST':
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     print("VALID");
        #     print(request.FILES)

        context = {'request': request}
        print(request.FILES)
        return render(request, 'file_demo/result.html', context)
