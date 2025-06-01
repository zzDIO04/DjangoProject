from django.db import models

# Create your models here.

# principal/models.py
from django.db import models

class PaginaInicial(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

