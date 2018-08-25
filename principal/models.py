from django.db import models

class comentario(models.Model):
    texto_comentario=models.TextField(default="Nada")
    direccion_correo=models.CharField(max_length=100, default="No ha introducido una dirección de correo")
    nombre=models.CharField(max_length=100, default="No ha introducido un nombre")
