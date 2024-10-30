from django.db import models

from core.usuario.models import Artist
from . import Song, Genre
from core.uploader.models import Image

class Album(models.Model):
    name = models.CharField(null=False, max_length=90)
    description = models.TextField(null=True, max_length=650)
    autor = models.ForeignKey(Artist, on_delete=models.PROTECT)
    songs = models.ForeignKey(Song, on_delete=models.PROTECT, null=True, blank=True)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name