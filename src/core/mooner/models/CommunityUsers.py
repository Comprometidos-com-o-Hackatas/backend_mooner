from django.db import models
from core.usuario.models import Usuario
from .community import Community

class CommunityUsers(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.email
