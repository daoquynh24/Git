from django.db import models

from core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'users.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)

    # modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
