from django.db import models
from django.utils.translation import ugettext_lazy as _

from .poll import Poll


class Choice(models.Model):
    content = models.CharField(
        _("Content"),
        max_length=100,
        blank=False,
        null=False)
    count = models.IntegerField(
        _("Content"),
        null=True,
        blank=True, 
        default=0)
    choice_note = models.CharField(
        _("choice_note"),
        max_length=100,
        blank=True,
        null=True)
    poll = models.ForeignKey(
        Poll,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")

    def __str__(self):
        return f"{self.content}"
