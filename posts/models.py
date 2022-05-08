from django.conf import settings
from django.db import models

from sorl.thumbnail import ImageField

from orbs.models import Orb


class Post(Orb):
    poster = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    thread = models.ForeignKey(
        "threads.Thread",
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    image = ImageField(
        upload_to='upload/',
        null=True,
        blank=True
    )
    file = models.FileField(
        null=True,
        blank=True
    )


class Reply(Post):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="replies",
    )
