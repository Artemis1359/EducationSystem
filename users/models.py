from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=200,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=200
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=200
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=200,
        unique=True
    )
