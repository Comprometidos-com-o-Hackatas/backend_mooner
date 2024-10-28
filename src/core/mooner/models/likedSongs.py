from django.db import models

from core.usuario.models import Usuario
from . import Song


class LikedSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(Usuario, on_delete=models.PROTECT)

def __str__(self):
    return self.song