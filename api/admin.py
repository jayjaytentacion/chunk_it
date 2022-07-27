from django.contrib import admin
from . models import Chunks, UploadedFile
# Register your models here.
admin.site.register(Chunks)
admin.site.register(UploadedFile)