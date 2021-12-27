from django.forms import ModelForm, TextInput, FileInput, Select, CheckboxInput
from .models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = (
            '__all__'
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter location name'}),
            'parent': Select(attrs={'class': 'form-control', 'id': 'address'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
            'image': FileInput(attrs={'class': 'file-upload-default', 'id': 'imageUpload'}),
        }

