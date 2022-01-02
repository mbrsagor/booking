from django.forms import ModelForm, TextInput, FileInput, Select, CheckboxInput, NumberInput, Textarea, EmailInput, \
    DateInput, CharField, PasswordInput, BooleanField, SelectMultiple
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Location, Rent, User, Booking, Profile


class UserLoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True,
               'autofocus': True}))
    password = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))
    remember_me = BooleanField(required=False)


class UserSignUpForm(UserCreationForm):
    password1 = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
        }


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            '__all__'
        )
        exclude = ('username', 'user_id')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'email': TextInput(attrs={'class': 'form-control', 'id': 'email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'marital_status': Select(attrs={'class': 'form-control', 'id': 'marital_status'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'id': 'date_of_birth', 'type': 'date'}),
            'nid_number': TextInput(attrs={'class': 'form-control', 'id': 'nid_number'}),
            'profile_picture': FileInput(attrs={'class': 'file-upload-default', 'id': 'profile_picture'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number')


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
            'discount_price': TextInput(attrs={'class': 'form-control', 'id': 'discount_price'}),
            'rent_location': Select(attrs={'class': 'form-control', 'id': 'rent_location'}),
            'types': Select(attrs={'class': 'form-control', 'id': 'types'}),
            'is_available': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_available'}),
            'is_ac': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_ac'}),
            'is_wifi': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_wifi'}),
            'is_tv': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_tv'}),
            'breakfast': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'breakfast'}),
            'is_lunch': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_lunch'}),
            'is_dinner': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_dinner'}),
            'descriptions': Textarea(
                attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter Description'}),
            'image': FileInput(attrs={'class': 'file', 'id': 'imageUpload'}),
            'gallery_image': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload'}),
            'gallery_image2': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload2'}),
            'gallery_image3': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload3'}),
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ('date_joined', 'password',)
        fields = (
            '__all__'
        )
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}),
            'role': Select(attrs={'class': 'form-control', 'id': 'role'}),
        }


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ('customer', 'customer_id',)
        fields = (
            '__all__'
        )
        widgets = {
            'rent_name': SelectMultiple(attrs={'class': 'prompt', 'id': 'rent_name'}),
            'status': Select(attrs={'class': 'form-control', 'id': 'status'}),
            'payment_type': Select(attrs={'class': 'form-control', 'id': 'payment_type'}),
            'address': TextInput(
                attrs={'class': 'form-control', 'id': 'address', 'placeholder': 'Enter your valid address'}),
            'booking_purpose': TextInput(attrs={'class': 'form-control', 'id': 'address',
                                                'placeholder': 'What purpose do you want to booking?'}),
            'transaction_id': TextInput(attrs={'class': 'form-control', 'id': 'transaction_id',
                                               'placeholder': '#38fzs37sf747'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number',
                                             'placeholder': 'Which phone number management will contact you'}),
            'booking_date': DateInput(attrs={'class': 'form-control', 'id': 'booking_date', 'type': 'date'}),
            'checkout_date': DateInput(attrs={'class': 'form-control', 'id': 'booking_date', 'type': 'date'}),
        }
