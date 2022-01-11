from django.forms import ModelForm
from myapp.models import TextFile


class FileUploadForm(ModelForm):
    class Meta:
        model = TextFile
        fields = ('name', 'title', 'file')
