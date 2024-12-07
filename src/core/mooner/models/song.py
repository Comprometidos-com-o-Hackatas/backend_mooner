from django.db import models
from core.uploader.models import Image, Document
from core.usuario.models import Artist
from .genre import Genre


class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    date_realized = models.DateField(auto_now_add=True)
    uploaded_on = models.DateField(auto_now=True)
    player = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    reproductions = models.IntegerField(default=0) 
    lyrics = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=None)
    background_dark_color = models.CharField(null='#000000', max_length=7)
    background_light_color = models.CharField(null='#000000', max_length=7)
   

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'
        ordering = ['-date_realized']
    
    def __str__(self) -> str:
        return f"{self.title} - {self.artists}"
