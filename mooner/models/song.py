from typing import Iterable
from django.db import models
from uploader.models import Image, Document
from django.core.exceptions import ValidationError
from .genre import Genre

class Song(models.Model):
    title = models.CharField(max_length=100, validators=[])
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    date_realized = models.DateField(auto_now_add=True)
    uploaded_on = models.DateField(auto_now=True)
    duration = models.DurationField()
    player = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    reproductions = models.IntegerField(default=0) 
    lyrics = models.TextField()
    genre = models.ManyToManyField(Genre)
    
    def __str__(self) -> str:
        return self.title
        