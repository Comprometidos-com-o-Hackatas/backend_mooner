from django.db import models
from core.uploader.models import Image, Document
from core.usuario.models import Usuario as User
from .genre import Genre


class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(User)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    date_realized = models.DateField(auto_now_add=True)
    uploaded_on = models.DateField(auto_now=True)
    duration = models.DurationField()
    player = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    reproductions = models.IntegerField(default=0) 
    lyrics = models.TextField()
    genre = models.ManyToManyField(Genre)
    country = models.CharField(max_length=50, default=None)
   

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'
        ordering = ['-date_realized']
    
    def __str__(self) -> str:
        return self.title
    
        