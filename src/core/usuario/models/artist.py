from django.db import models
from .usuario import Usuario
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from uuid import uuid4
from rest_framework.response import Response
from rest_framework import status
from core.email_verification.send_email_verification_artist import send_email_to_user_to_be_an_artist



class Artist(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    artistic_name = models.CharField(max_length=100, blank=True, null=True)
    following = models.IntegerField(default=0, blank=True, null=True)
    followers = models.IntegerField(default=0, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)


@receiver(post_save, sender=Artist)
def send_email_verification_to_become_artist(sender, instance, created, **kwargs):
    print('sinal chamado')
    if created:
        user = Usuario.objects.get(id=instance.user.id)
        token = str(uuid4())

        print('usuario chamado')

        user.token_verification = token
        user.save()

        url = reverse('verify_email', kwargs={'verification_token': token})

        try:
            send_email_to_user_to_be_an_artist(user_id=user.id, verify_url=url)
        except ValueError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': e})
