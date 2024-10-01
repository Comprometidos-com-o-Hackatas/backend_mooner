from django.db import models
from core.uploader.models import Image

class Producer(models.Model):
    followers = models.IntegerField(default=0)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    name = models.CharField(max_length=50)
    realized = models.DateField(auto_now=True)
    about = models.TextField()

    def __str__(self) -> str:
        return self.name