from django.db import models

class comentario(models.Model):
    texto_comentario=models.TextField(default="Nada")
    direccion_correo=models.CharField(max_length=100, default="No ha introducido una dirección de correo")
    nombre=models.CharField(max_length=100, default="No ha introducido un nombre")

class pregunta(models.Model):
    universidad=models.CharField(max_length=100, default="No ha introducido una universidad")
    grado=models.CharField(max_length=100, default="No ha introducido un grado")
    pregunta=models.TextField(default="No ha introducido un comentario")
    detalles=models.TextField(default="No ha introducido detalles")
    email=models.CharField(default="No ha introducido email", max_length=100)

class falta(models.Model):
    texto_falta=models.TextField(default="No ha introducido nada que falte")