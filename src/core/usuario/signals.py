from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from uuid import uuid4
from core.usuario.models import Artist
from core.usuario.models import Usuario as User
from rest_framework.response import Response
from rest_framework import status
from email_verification.send_email_verification_artist import send_email_to_user_to_be_an_artist

@receiver(post_save, sender=Artist)
def send_email_verification_to_become_artist(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(id=instance.id)
        token = str(uuid4())

        user.token_verification = token
        user.save()

        url = reverse('verify_email', kwargs={'verification_token': token})

        try:
            send_email_to_user_to_be_an_artist.delay(user_id=user.id, verify_url=url)
        except ValueError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': e})

