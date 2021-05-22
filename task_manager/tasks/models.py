from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import Category
from core.models import BaseModel


class Task(BaseModel):
    name = models.CharField(_("name"), max_length=150)
    description = models.TextField(_("description"), default="", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        related_query_name="task",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="tasks",
        related_query_name="task",
    )
    is_completed = models.BooleanField(_("completed"), default=False)
    date = models.DateTimeField(_("date"))

    class Meta:
        ordering = ["author", "-date"]
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
