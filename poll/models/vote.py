from django.db import models
from django.utils.translation import ugettext_lazy as _

from voter.models import VoterUser
from .poll import Poll


class Vote(models.Model):
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
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now=False,
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        auto_now_add=False)

    class Meta:
        verbose_name = _("vote")
        verbose_name_plural = _("votes")
        unique_together = (('poll', 'voter'))

    def __str__(self):
        return f"{self.voter} : {self.poll}"
