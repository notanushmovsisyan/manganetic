from django.db import models
from django.contrib.auth.models import (
    AbstractUser, PermissionsMixin
)
from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = AbstractUser.username
    email = models.EmailField(max_length=254, unique=True)
    #  bookmarks = models.ForeignKey(Manga, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


