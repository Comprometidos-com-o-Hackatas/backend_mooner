from django.db import models
from core.usuario.models import Artist
from . import  Community
from core.uploader.models import Image

class CommunityPosts(models.Model):
    description = models.TextField(null=True, max_length=850)
    autor = models.ForeignKey(Artist, on_delete=models.PROTECT)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    dislikes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.description
    

    
