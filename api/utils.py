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
media_path='/media/'
base_dir = settings.MEDIA_ROOT


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
  #opens uploaded file
  with open(in_file_path,'r') as f:
    #validates it
    try:
        #stores the object in a list
        json_obj_list = json.load(f)
    except:
       print("Not working could not load json file")
    #set prefixes for each individual file  
    index=0
    #gets the media folder
      #i've made the base dir global
    #creates a new dir to store the chunks
    os.makedirs(base_dir + "/json/")#to be renamed so that two folders never have the same name
    #loops through the objs in the list
    for json_obj in range(0,len(json_obj_list), objs_per_split):
        index=index+1
        filename=base_dir+"/json/"+str(index)+'.json'

        with open(filename, 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`    
            hey=json_obj_list[json_obj:json_obj + objs_per_split]
            json.dump(hey, out_json_file, indent=4)
            directory=pathlib.Path(base_dir + "/json/")    
            return directory,f      

def zipper_function(directory,f):
          # # the first parameter in zipfile.Zipfile is the location where the zip file is saved
          #zip location
          zip_location=base_dir + "/" + 'chunk.zip'# later to add the name of file with uuid
          with zipfile.ZipFile(zip_location, "w", ZIP_DEFLATED, compresslevel=2) as archive:
            for file_path in directory.iterdir():
              archive.write(file_path, arcname=file_path.name)
            archive.close()
          shutil.rmtree(directory)
          # this code is responsible for deleting the initial uploaded file
          dir_path = Path(__file__).resolve().parent / "media"
          file_path = dir_path / f.name
          file_path.unlink() # remove file
          return media_path +'chunk.zip'

 
def generateUUID():

    return str(uuid.uuid4()) + ".zip"
