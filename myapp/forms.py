from django import forms
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'description', 'pet_image']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']