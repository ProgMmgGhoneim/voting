from django.db import models
from django.utils.translation import ugettext_lazy as _

from voter.models import VoterUser
from .poll import Poll


class Comment(models.Model):
    content = models.CharField(
        _("Content"),
        max_length=100,
        blank=True,
        null=True)
    poll = models.ForeignKey(
        Poll,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    voter = models.ForeignKey(
        VoterUser,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"{self.content}"
