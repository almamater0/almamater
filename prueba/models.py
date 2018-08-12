from django.db import models

class p(models.Model):
    texto = models.TextField(default="¡")
    username = models.CharField(max_length=30)
