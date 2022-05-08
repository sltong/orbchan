import uuid

from model_utils.models import TimeStampedModel

from django.db import models


class Orb(TimeStampedModel, models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
