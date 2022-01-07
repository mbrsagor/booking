from django.forms import ModelForm, TextInput, FileInput, Select, CheckboxInput, NumberInput, Textarea

from rent.models import Location, Rent


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


class RentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)
        self.fields['rent_location'].queryset = Location.objects.filter(is_active=True)

    class Meta:
        model = Rent
        fields = (
            '__all__'
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter location name'}),
            'bed_room': NumberInput(attrs={'class': 'form-control', 'id': 'bed_room'}),
            'bath_room': NumberInput(attrs={'class': 'form-control', 'id': 'bath_room'}),
            'price': TextInput(attrs={'class': 'form-control', 'id': 'price'}),
            'rent_location': Select(attrs={'class': 'form-control', 'id': 'rent_location'}),
            'types': Select(attrs={'class': 'form-control', 'id': 'types'}),
            'is_available': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_available'}),
            'descriptions': Textarea(
                attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter Description'}),
            'image': FileInput(attrs={'class': 'file', 'id': 'imageUpload'}),
            'gallery_image': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload'}),
            'gallery_image2': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload2'}),
            'gallery_image3': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload3'}),
        }
