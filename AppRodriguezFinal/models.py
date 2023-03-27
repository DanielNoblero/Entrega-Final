from django.db import models

class Receta(models.Model):
    Nombre_de_receta= models.CharField(max_length=30)
    Autor= models.CharField(max_length=15)
    Rendimiento = models.CharField(max_length=10)
    Tiempo_de_prepracion= models.CharField(max_length=50)