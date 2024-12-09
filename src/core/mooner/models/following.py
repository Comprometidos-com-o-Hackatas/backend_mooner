from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from core.usuario.models import Usuario, Artist

class Following(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=None, blank=True, null=True, related_name='user')
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, default=None, blank=True, null=True, related_name='artist')

    def __str__(self):
        return self.user.email
    
@receiver(post_save, sender=Following)
def update_followers_on_create(sender, instance, created, **kwargs):
    if created:
        instance.user.following += 1
        instance.user.save()
        instance.artist.followers += 1
        instance.artist.save()

@receiver(post_delete, sender=Following)
def update_followers_on_delete(sender, instance, **kwargs):
    instance.user.following -= 1
    instance.user.save()
    instance.artist.followers -= 1
    instance.artist.save()