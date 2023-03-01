from django.forms import ModelForm
from .models import FileUpload

class UploadForm(ModelForm):
    class Meta: 
        model = FileUpload
        fields = '__all__'
