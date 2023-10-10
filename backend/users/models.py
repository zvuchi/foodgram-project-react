from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole:
    USER = "user"
    ADMIN = "admin"
    choices = [(USER, "USER"), (ADMIN, "ADMIN")]


class User(AbstractUser):
    username = models.CharField(
        "Имя пользователя",
        max_length=150,
        unique=True,
        null=True,
    )
    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    email = models.EmailField(
        "Элетронная почта",
        max_length=254,
        unique=True,
    )
    role = models.TextField(
        choices=UserRole.choices,
        default=UserRole.USER,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.username
