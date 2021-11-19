from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    tell = models.CharField(max_length=13, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
