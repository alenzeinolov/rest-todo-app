from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(_("name"), unique=True, max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories",
        related_query_name="category",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("category")
        verbose_name_plural = _("categories")
