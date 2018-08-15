from django.db import models

class comentario(models.Model):
    texto_comentario=models.TextField(default="Nada")
