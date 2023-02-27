from django.forms import ModelForm
from .models import FileUpload

class BeastForm(ModelForm):
    class Meta: 
        model = FileUpload
        fields = '__all__'
