from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'sex', 'username', 'password']

class LogInForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario:', max_length=50)
    password = forms.CharField(label='Contraseña:', max_length=50)
