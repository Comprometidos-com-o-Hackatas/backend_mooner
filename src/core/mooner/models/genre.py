from django.db import models

class Genre(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.description