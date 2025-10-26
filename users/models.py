from django.db import models

# Create your models here.

class User(models.Model):
    "Información del usuario." 
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=6)

    def __str__(self):
        return self.name


    

