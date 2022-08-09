import uuid

from django.db import models
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils.models import TimeStampedModel
from treebeard.mp_tree import MP_Node


class Orb(TimeStampedModel, models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Category(MP_Node, Orb):
    name = models.CharField(max_length=63)

    node_order_by = ['name']

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
    abbreviation = models.CharField(max_length=15)
    slug = models.CharField(
        _("slug"),
        max_length=31
    )

    def save(self, *args, **kwargs):
        if not self.abbreviation:
            self.abbreviation = self.get_abbreviation_from_name()
        super().save(*args, **kwargs)

    def get_abbreviation_from_name(self):
        abbreviation = ""
        words = self.name.split()
        for word in words:
            abbreviation += str(words[0]).lower()
        return abbreviation

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("board", kwargs={"board_slug": self.slug})


class Thread(Orb):
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="threads",
    )
    subject = models.CharField(
        max_length=127
    )

    def __str__(self):
        return self.subject


class RepliesManager(models.Manager):
    def replies(self):
        return self.objects.order_by("id")[:1]


class Post(Orb):
    poster = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    text = models.TextField()
    image = ThumbnailerImageField(
        upload_to='upload/',
        null=True,
        blank=True
    )
    file = models.FileField(
        null=True,
        blank=True
    )

    objects = models.Manager()
    replies = RepliesManager()

    def __str__(self):
        return f"{self.thread} post {self.id}"

    def is_original_post(self):
        """
        Returns true if the post is the original to its thread.
        """
        return True if self is self.thread.posts.first() else False
