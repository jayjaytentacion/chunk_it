# this is the views that contains the functionality of the chunk_it application
from django.core.files.base import ContentFile
from django.shortcuts import render, HttpResponse, redirect
from .forms import UploadFileForm
from . utils import handle_uploaded_file, ChunkJson, os
from django.conf import settings
from . models import ChunkOrder



def DashBoardView(request):
    # the dashboard view could be modified to be a single TemplateView 
    # but for easy of use we will make use a function based view
    upload_form = UploadFileForm()
    # first we check if a session exists and the value is not zero
    # if that is successfull then we show the currently uploaded file
    context = {"uploadform": upload_form}
    return render(request, "api/dashboard.html", context)
       

def StartChunking(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = handle_uploaded_file(request.FILES['file'])
            chunk_size = form.cleaned_data['size']
            file_name = request.FILES['file'].name
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            ChunkJson(file_path, chunk_size)
            zip = "/media/chunk.zip"
            order = ChunkOrder.objects.create(zip = zip, file_name = file_name, chunk_size = chunk_size)
            return render(request, 'api/test.html', context = {"download":order.zip})

    else:
        form = UploadFileForm()
    return redirect("dashboard")


# def UploadFileView(request):
#     # this view is responsible for the uploading and storing of json or csv files
#     # on the server
#     # we will be using sessions to keep track of the files that have been uploaded
#     if request.method == "POST":
#         file = UploadForm(request.POST, request.FILES)
#         if file.is_valid():
#             temp_file = file.save(commit=False)
#             temp_file.filename = request.FILES['file'].name
#             temp_file.save()
#             request.session['current_upload'] = temp_file.id
#             print(request.session['current_upload'])
#             # after the file has been uploaded then redirect the user to the dashboard
#             return redirect("dashboard")
#         else: 
#             # the right file was not submitted
#             raise ValidationError("We currently only support CSV and JSON")

# def ChunkFileView(request):
#     # this view is responsible for the chunking processes
#     # most of the logic for chunking will be referenced in the utils.py files
#     # first we check to see if a file has been recently uploaded
#     try: 
#         current_file = request.session["current_upload"]
#         print(current_file)
#     except:
#         return redirect("dashboard")
#     if current_file  != 0:
#         del request.session["current_upload"]
#         # if there is a current file then we can proceed to validate the file
#         target_file = UploadedFile.objects.get(id = current_file)
#         context = {"file": target_file}
#         return render(request, 'api/test.html', context)