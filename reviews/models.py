from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    contenido = models.TextField()
    canción_fav = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario} - {self.artista} - {self.album}"
