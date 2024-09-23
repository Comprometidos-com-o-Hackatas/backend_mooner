from django.db import models
from usuario.models import Usuario as User
from django.dispatch import receiver
from django.db.models.signals import post_save
from config.ia_config import chat_session

class LunaAI(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    response = models.TextField(null=True, blank=True)

@receiver(post_save, sender=LunaAI)
def get_luna_response(instance, created, sender, **kwargs):
    if created:
        luna_response = chat_session.send_message(instance.answer)
        instance.response = luna_response.text
        instance.save(update_fields=['response'])
        print(luna_response.text)

    