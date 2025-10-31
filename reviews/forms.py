from django import forms
from .models import Review

class FormularioReseña(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['artista', 'album', 'contenido', 'canción_fav',]



