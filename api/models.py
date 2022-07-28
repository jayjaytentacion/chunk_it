from django.db import models
from django.contrib.auth import get_user_model
from . utils import ValidateFile
# Create your models here.


class ChunkOrder(models.Model):
    custom_user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='custom_User', null=True, blank=True)
    zip= models.FileField(upload_to="largefile", validators=[ValidateFile])
    file_name = models.CharField(max_length=20, blank=True, null=True)
    chunk_size=models.IntegerField()

    def __str__(self) -> str:
        return self.filename

# my name is sydney


# class Chunks(models.Model):
#     uploadedfile = models.ForeignKey(
#         UploadedFile, on_delete=models.CASCADE, related_name="uploadedfile", blank=True, null=True)
#     chunk = models.FileField(upload_to="chunks", blank=True, null=True)
#     chunksize = models.IntegerField()
