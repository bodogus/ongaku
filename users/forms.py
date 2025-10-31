#Esto es para el formulario de crear cuenta.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Esto es para el formulario de inicio de sesión.
from django.contrib.auth.forms import AuthenticationForm

class RegistroFormulario(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario",)
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Repite la contraseña")
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


