from django.forms import ModelForm, TextInput, FileInput, Select, EmailInput, \
    DateInput, CharField, PasswordInput, BooleanField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from rent.models import User, Profile


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
