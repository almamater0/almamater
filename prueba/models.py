from django.db import models

class prueba(models.Model):
    texto = models.TextField(default="¡")
    username = models.CharField(max_length=30)
