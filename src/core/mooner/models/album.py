from django.db import models

from core.usuario.models import Usuario
from . import Song

class Album(models.Model):
    artist = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    songs = models.ManyToManyField(Song)

def __str__(self):
    return self.song