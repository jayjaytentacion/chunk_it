from distutils.command.upload import upload
from django.shortcuts import render, HttpResponse
from . forms import UploadedFile, ChunkForm

# Create your views here.
def UploadView(request):
    uploadFile = UploadedFile()
    context = {"form": uploadFile}
    return render(request, "api/dashboard.html", context)