from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class UploadedFile(models.Model):
    cutomuser = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='customUser', null=True, blank=True)
    file = models.FileField(upload_to="largefile")
    filename = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.filename


class Chunks(models.Model):
    uploadedfile = models.ForeignKey(
        UploadedFile, on_delete=models.CASCADE, related_name="uploadedfile", blank=True, null=True)
    chunk = models.FileField(upload_to="chunks", blank=True, null=True)
    chunksize = models.IntegerField()
