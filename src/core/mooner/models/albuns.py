from django.db import models

from core.usuario.models import Artist
from . import Song, Genre
from core.uploader.models import Image
import datetime

class Album(models.Model):
    name = models.CharField(null=False, max_length=90)
    autor = models.ForeignKey(Artist, on_delete=models.PROTECT)
    songs = models.ManyToManyField(Song)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    background_dark_color = models.CharField(null='#000000', max_length=7)
    background_light_color = models.CharField(null='#000000', max_length=7)
    date_realized = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name