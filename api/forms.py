from django.forms import ModelForm
from api.models import UploadedFile,Chunks



class UploadForm(ModelForm):
    class Meta:
        model=UploadedFile
        fields=['file']


class ChunkForm(ModelForm):
    class Meta:
        model=Chunks
        fields=['chunksize']
