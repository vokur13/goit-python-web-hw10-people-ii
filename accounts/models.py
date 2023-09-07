from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class GenderType(models.TextChoices):
        MALE = (
            "m",
            "male",
        )
        FEMALE = (
            "f",
            "female",
        )
        OTHER = "o", "other"

    gender = models.CharField(null=True, blank=True,
                              max_length=1, choices=GenderType.choices, default=GenderType.MALE
                              )
