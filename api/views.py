# this is the views that contains the functionality of the chunk_it application
from django.forms import ValidationError
from django.shortcuts import render, HttpResponse, redirect
from .forms import UploadForm, ChunkSizeForm
from .models import UploadedFile



def DashBoardView(request):
    # the dashboard view could be modified to be a single TemplateView 
    # but for easy of use we will make use a function based view
    upload_form = UploadForm()
    chunk_size_form = ChunkSizeForm()
    # first we check if a session exists and the value is not zero
    # if that is successfull then we show the currently uploaded file
    current_file = request.session.get("current_upload", 0)
    if current_file != 0:
        fileInstance = UploadedFile.objects.get(id = request.session["current_upload"])
        upload_form = UploadForm(instance = fileInstance)
    
        
    context = {"uploadform": upload_form, "chunksizeform": chunk_size_form}
    return render(request, "api/dashboard.html", context)
       



def UploadFileView(request):
    # this view is responsible for the uploading and storing of json or csv files
    # on the server
    # we will be using sessions to keep track of the files that have been uploaded
    if request.method == "POST":
        file = UploadForm(request.POST, request.FILES)
        if file.is_valid():
            temp_file = file.save(commit=False)
            temp_file.filename = request.FILES['file'].name
            temp_file.save()
            request.session['current_upload'] = temp_file.id
            print(request.session['current_upload'])
            # after the file has been uploaded then redirect the user to the dashboard
            return redirect("dashboard")
        else: 
            # the right file was not submitted
            raise ValidationError("We currently only support CSV and JSON")

def ChunkFileView(request):
    # this view is responsible for the chunking processes
    # most of the logic for chunking will be referenced in the utils.py files
    # first we check to see if a file has been recently uploaded
    try: 
        current_file = request.session["current_upload"]
        print(current_file)
    except:
        return redirect("dashboard")
    if current_file  != 0:
        del request.session["current_upload"]
        # if there is a current file then we can proceed to validate the file
        target_file = UploadedFile.objects.get(id = current_file)
        context = {"file": target_file}
        return render(request, 'api/test.html', context)