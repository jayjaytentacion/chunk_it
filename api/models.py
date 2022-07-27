from distutils.command import upload
from django.db import models
from accounts.models import CustomUser

# Create your models here.


class UploadedFile(models.Model):
    cutomuser = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='custom user')
    file = models.FieldFile(upload_to="largefile")
    fiename = models.CharField(max_length=20)


class Chunks(models.Model):
    uploadedflie = models.ForeignKey(
        UploadedFile, on_delete=models.CASCADE, related_name="uploadedflie")
    chunk = models.FileField(upload_to="chunks")
    chunksize = models.IntegerField()
