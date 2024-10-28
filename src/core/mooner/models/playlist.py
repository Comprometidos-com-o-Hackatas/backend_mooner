from django.db import models

from core.usuario.models import Usuario
from . import Song

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    owners = models.ManyToManyField(Usuario)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name    