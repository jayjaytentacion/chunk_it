from distutils.command import upload
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

<<<<<<< HEAD
class UploadedFile(models.Model):
    cutomuser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='custom user')
    file=models.FieldFile(upload_to="largefile")
    fiename=models.CharField(max_length=20)


class Chunks(models.Model):
    uploadedflie=models.ForeignKey(UploadedFile,on_delete=models.CASCADE,related_name="uploadedflie")
    chunk=models.FileField(upload_to="chunks")
    chunksize=models.IntegerField()
=======

class UploadedFile(models.Model):
    cutomuser = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='custom user')
    file = models.FieldFile(upload_to="largefile")
    fiename = models.CharField(max_length=20)


class Chunks(models.Model):
    uploadedflie = models.ForeignKey(
        UploadedFile, on_delete=models.CASCADE, related_name="uploadedfile")
    chunk = models.FileField(upload_to="chunks")
    chunksize = models.IntegerField()
>>>>>>> 14c78b7f79d844def10601fc79017be444f528d2
