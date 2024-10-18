from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.uploader.models import Image

from .managers import CustomUserManager

TYPE_USER = [
    ('normaluser', 'NormalUser'),
    ('produtor', "Produtor"),
    ('artista', 'Artista')
]

class Usuario(AbstractUser):
    username = None
    perfil = models.ForeignKey(Image, on_delete=models.CASCADE)
    email = models.EmailField(_("e-mail address"), unique=True)
    about = models.TextField(null=True, blank=False)
    DDD = models.CharField(max_length=5, null=True, blank=True)
    telephone = models.CharField(max_length=11, null=True, blank=True)
    followers = models.IntegerField(default=0)
    folowing = models.IntegerField(default=0)
    type_user = models.CharField(max_length=10, choices=TYPE_USER, default='NormalUser')
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
