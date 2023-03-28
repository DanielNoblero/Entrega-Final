from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    Nombre_de_receta= models.CharField(max_length=30)
    Autor= models.CharField(max_length=15)
    Rendimiento = models.CharField(max_length=10)
    Horas_de_prepracion= models.CharField(max_length=50)
