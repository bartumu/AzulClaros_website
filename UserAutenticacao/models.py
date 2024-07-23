from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from FuncDashboard.models import *


class Usuario(AbstractUser):
    """ USER_TYPE_CHOICES = (
        ('cliente', 'Cliente'),
        ('funcionario', 'Funcionário'),
    ) """

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    #user_tipo = models.CharField(max_length=14, choices=USER_TYPE_CHOICES, default='cliente')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_tipo']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email
