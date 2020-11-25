from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'telefono', 'first_name', 'last_name')

class BaseForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
