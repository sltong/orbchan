from django.db import models

from orbs.models import Orb


class Thread(Orb):
    board = models.ForeignKey(
       "boards.Board",
        on_delete=models.CASCADE,
        related_name="threads",
    )
    subject = models.CharField(
        max_length=127
    )

    def __str__(self):
        return self.subject
