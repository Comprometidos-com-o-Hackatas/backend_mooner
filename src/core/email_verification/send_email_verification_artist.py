from core.usuario.models import Usuario as User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from celery import shared_task

@shared_task
def send_email_to_user_to_be_an_artist(user_id, verify_url):
    user = User.objects.get(id=user_id)
    link_verfication = f'http://localhost:8000{verify_url}'
    
    html_render = render_to_string('verification.html', {
        'email': user.email,
        'verify': link_verfication 
    })

    email_multi_alternative = EmailMultiAlternatives(
        'Email de verificação',
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )

    email_multi_alternative.attach_alternative(html_render, 'text/html')
    email_multi_alternative.send()

    print(user.email)

    return Response(status=status.HTTP_200_OK, data={'msg': f'email enviado para {user.email}'})


