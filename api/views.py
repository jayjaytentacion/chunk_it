from distutils.command.upload import upload
from django.shortcuts import render, HttpResponse
from . forms import UploadForm, ChunkForm
from  . models import UploadedFile
# Create your views here.
def UploadView(request):
    if request.method == "POST":
         uploadFile = UploadForm(request.POST, request.FILES)
         if uploadFile.is_valid():
            file = uploadFile.save(commit = False)
            file.filename = request.FILES['file'].name
            file.save()
    else:
        uploadFile = UploadForm()
    
    chunckSetting = ChunkForm()
    context = {"upload": uploadFile, "chunk": chunckSetting}
    return render(request, "api/dashboard.html", context)

