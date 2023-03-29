from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
        Nombre_de_receta= models.CharField(max_length=30)
        Autor= models.CharField(max_length=15)
        Rendimiento = models.CharField(max_length=10)
        Horas_de_prepracion= models.CharField(max_length=50)
        Preparacion=models.TextField(max_length=5000)
        Publicador= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher") 
        image = models.ImageField(upload_to="recetas", null=True, blank=True)
        creado_el = models.DateTimeField(auto_now_add=True)

        @property
        def image_url(self):
                return self.image.url if self.image else ''

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
        avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

        @property
        def avatar_url(self):
                return self.avatar.url if self.avatar else ''

class Mensaje(models.Model):
        mensaje = models.TextField(max_length=1000)
        email = models.EmailField()
        creado_el = models.DateTimeField(auto_now_add=True) 
        destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")