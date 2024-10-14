from django.db import models
from core.usuario.models import Usuario as User
from .song import Song
from simple_history.models import HistoricalRecords

class History(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default=None, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    history = HistoricalRecords()
    

    def __str__(self) -> str:
        return f'{self.usuario} - {self.song}'
    

    

        
    
