
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subTitulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor
