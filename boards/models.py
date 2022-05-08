from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField

from orbs.models import Orb


class Category(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class Board(Orb):
    name = models.CharField(
        _("name"),
        max_length=63
    )
    description = models.CharField(
        _("description"),
        max_length=255
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name=_("boards")
    )
    slug = models.CharField(
        _("slug"),
        max_length=31
    )

    def get_abbreviation_from_name(self):
        abbreviation = ""
        words = self.name.split()
        for word in words:
            abbreviation += str(words[0]).lower()
        return abbreviation

    def __str__(self):
        return self.name
