from django import forms
from pond_app.models import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        exclude=[u'location']
        