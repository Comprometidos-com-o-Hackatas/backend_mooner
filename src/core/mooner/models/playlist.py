from django.db import models

from core.usuario.models import Usuario
from . import Song
from core.uploader.models import Image

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    owners = models.ManyToManyField(Usuario)
    songs = models.ManyToManyField(Song, null=True, blank=True)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')

    def __str__(self):
        return self.name    