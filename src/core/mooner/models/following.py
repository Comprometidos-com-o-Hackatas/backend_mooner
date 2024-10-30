from django.db import models

from core.usuario.models import Usuario, Artist

class Following(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=None, blank=True, null=True, related_name='user')
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, default=None, blank=True, null=True, related_name='artist')

    def __str__(self):
        return self.user