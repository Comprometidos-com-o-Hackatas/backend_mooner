from django.db import models

from core.usuario.models import Usuario
from . import Genre
from core.uploader.models import Image

class Community(models.Model):
    name = models.CharField(null=False, max_length=160)
    description = models.TextField(null=True, max_length=850)
    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name