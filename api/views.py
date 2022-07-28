from distutils.command.upload import upload
from django.shortcuts import render, HttpResponse
from . forms import UploadForm, ChunkForm
from  . models import UploadedFile
# Create your views here.

def DashBoardView(request):
    # this view is responsible for the uploading of the JSON and CSV files
    # it also contains a form that will set the integer field and file size to chunk by
    chunk_form = ChunkForm()
    if request.method == "POST":
         uploadFile = UploadForm(request.POST, request.FILES)
         if uploadFile.is_valid():
            file = uploadFile.save(commit = False)
            file.filename = request.FILES['file'].name
            request.session["fileId"] = file.id;
            file.save()
    else:
        uploadFile = UploadForm()

    context = {"upload": uploadFile, "chunk_form": chunk_form}
    return render(request, "api/dashboard.html", context)


def ChunkView(request):
    try:
        userFiles = request.session["fileId"];
        print(userFiles)
    except:
        print("fileId session does not exist yet, you have to upload a file")
        return HttpResponse("Failed")

    
    if request.method == "POST":
        chunk = ChunkForm(request.POST)
        del request.session["fileId"]
        return HttpResponse("Successful")
