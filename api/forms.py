from random import choices
from django import forms
from django.forms import ModelForm, Form
from django import forms
from . utils import ValidateFile

class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, validators=[ValidateFile])
    size=forms.IntegerField(required=True)


# class ChunkOrderForm(ModelForm):
#     class Meta:
#         model=UploadedFile
#         fields=['file','chunk_size']


# class ChunkForm(ModelForm):
#     class Meta:
#         model=Chunks
#         fields=['chunksize']


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
