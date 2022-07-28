# this file contains pure python logic for file validation 
# file chunking and chunk zipping 
import os
from django.forms import ValidationError

def ValidateFile(UploadedFile):
    # this serves as validation for the Upload file form in django
    file_name = str(UploadedFile)
    if UploadedFile.name.endswith('.csv') or UploadedFile.name.endswith(".json"):
        return UploadedFile
    else:
        raise ValidationError("Only CSV and JSON files are permitted")


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
