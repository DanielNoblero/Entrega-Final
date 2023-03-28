from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    Nombre_de_receta= models.CharField(max_length=30)
    Autor= models.CharField(max_length=15)
    Rendimiento = models.CharField(max_length=10)
    Horas_de_prepracion= models.CharField(max_length=50)
    Preparacion=models.CharField(max_length=1000)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher") 
    image = models.ImageField(upload_to="recetas", null=True, blank=True)


    def __str_(self):
        return f"{self.id} - {self.Nombre_de_receta}"
    
    @property
    def image_url(self):
        return self.image.url if self.image else ''

    def __str__(self):
        return f"{self.id} - {self.Nombre_de_receta} - {self.publisher.username}"
