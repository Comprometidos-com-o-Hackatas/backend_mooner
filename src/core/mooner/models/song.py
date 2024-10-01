from typing import Iterable
from django.db import models
from core.uploader.models import Image, Document
from .genre import Genre
from .producer import Producer

class Song(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    date_realized = models.DateField(auto_now_add=True)
    uploaded_on = models.DateField(auto_now=True)
    duration = models.DurationField()
    player = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    reproductions = models.IntegerField(default=0) 
    lyrics = models.TextField()
    genre = models.ManyToManyField(Genre)
    country = models.CharField(max_length=50, default=None)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'
        ordering = ['-date_realized']
    
    def __str__(self) -> str:
        return self.title
    
        