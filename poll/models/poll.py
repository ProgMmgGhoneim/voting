from django.db import models
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    titile = models.CharField(
        _("Titile"),
        max_length=100,
        blank=True,
        null=True)
    description = models.TextField(
        _("Description"),
        max_length=100,
        blank=True,
        null=True)
    expire_date = models.DateTimeField(
        _("When Poll expire?"),
        blank=True,
        null=True)
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now=False,
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        auto_now_add=False)
    
    class Meta:
        verbose_name = _("Poll")
        verbose_name_plural = _("Polls")

    @property
    def is_expire(self):
        return True
    
    def __str__(self):
        return f"{self.titile}"
