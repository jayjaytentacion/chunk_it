from random import choices
from django import forms
from django.forms import ModelForm, Form
from api.models import UploadedFile,Chunks
from django import forms



class UploadForm(ModelForm):
    class Meta:
        model=UploadedFile
        fields=['file']


class ChunkForm(ModelForm):
    class Meta:
        model=Chunks
        fields=['chunksize']


# class ChunkSizeForm(forms.Form):
#     sized_choices = (
#         ("KB", "Kilobytes"),
#         ("MB", "Megabytes"),
#         ("GB", "Gigabytes"),)
    
#     size_type = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.RadioSelect,
#         choices=sized_choices,
#     )
#     chunk_size = forms.IntegerField(required=True)
