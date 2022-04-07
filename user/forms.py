from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',
                  'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address']


class UpdateProfileForm(forms.ModelForm):
    phone = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = Profile
        fields = ['image', 'bio']
