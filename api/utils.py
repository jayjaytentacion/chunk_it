# this file contains pure python logic for file validation 
# file chunking and chunk zipping 
import json
import zipfile
import os
import pathlib
from pathlib import Path
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from django.forms import ValidationError
from django.conf import settings
import uuid



def ValidateFile(UploadedFile):
    # this serves as validation for the Upload file form in django
    file_name = str(UploadedFile)
    if UploadedFile.name.endswith('.csv') or UploadedFile.name.endswith(".json"):
        return UploadedFile
    else:
        raise ValidationError("Only CSV and JSON files are permitted")


def handle_uploaded_file(f):
    with open('media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return destination




def ChunkJson(in_file_path, objs_per_split):
  with open(in_file_path,'r') as f:
    try:
        json_obj_list = json.load(f)
    except:
       print("Not working could not load json file")
    index=0
    base_dir = settings.MEDIA_ROOT
    os.makedirs(base_dir + "/json/")
    for json_obj in range(0,len(json_obj_list), objs_per_split):
       # print(json_obj_list[json_obj])
        index=index+1
        filename=base_dir+"/json/"+str(index)+'.json'

        with open(filename, 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`    
            hey=json_obj_list[json_obj:json_obj + objs_per_split]
            json.dump(hey, out_json_file, indent=4)


  directory=pathlib.Path(base_dir + "/json/")
  # the first parameter in zipfile.Zipfile is the location where the zip file is saved
  with zipfile.ZipFile(base_dir + "/" + generateUUID(), "w", ZIP_DEFLATED, compresslevel=2) as archive:
    for file_path in directory.iterdir():
      archive.write(file_path, arcname=file_path.name)
    archive.close()
  shutil.rmtree(directory)
  # this code is responsible for deleting the initial uploaded file
  dir_path = Path(__file__).resolve().parent / "media"
  file_path = dir_path / f.name
  file_path.unlink() # remove file
<<<<<<< HEAD
=======

>>>>>>> e4da6a6e9885a9987c0dca62a7812b2ee3426e6b

 
def generateUUID():

    return str(uuid.uuid4()) + ".zip";
