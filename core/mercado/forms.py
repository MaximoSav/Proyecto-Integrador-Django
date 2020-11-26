from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'telefono', 'first_name', 'last_name')

class BaseForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100, required=False)
    la_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)

class ConfigForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(max_length=100)

    class Meta:
        model= User
        fields = ('email', 'telefono', 'first_name', 'last_name')