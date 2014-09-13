from django import forms
from pond_app.models import FileUpload

class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload