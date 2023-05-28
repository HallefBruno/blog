
from django.utils import timezone
from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subTitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor
