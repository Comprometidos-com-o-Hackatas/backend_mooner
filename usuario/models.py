from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    passage_id = models.CharField(max_length=255, unique=True)
    is_artist = models.BooleanField(default=False)
    about = models.TextField(null=True, blank=False)
    is_producer = models.BooleanField(default=False)
    DDD = models.CharField(max_length=5, default=None)
    telephone = models.CharField(max_length=11, default=None)
    followers = models.IntegerField(default=0)

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
