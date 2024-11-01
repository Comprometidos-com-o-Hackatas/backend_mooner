from django.db import models

from core.usuario.models import Usuario
from . import Song, Genre
from core.uploader.models import Image
import datetime

class Album(models.Model):
    name = models.CharField(null=False, max_length=90)
    description = models.TextField(null=True, max_length=650)
    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    songs = models.ForeignKey(Song, on_delete=models.PROTECT, null=True)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    date_realized = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name