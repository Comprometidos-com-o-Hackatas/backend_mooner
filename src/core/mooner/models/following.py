from django.db import models

from core.usuario.models import Usuario

class Following(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='user')
    artist = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='artist')

    def __str__(self):
        return self.user