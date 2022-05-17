from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class APItoken(models.Model):
    
    key = models.CharField(
        _("Key"), 
        max_length=256, 
        blank=False, 
        null=False)
    type = models.CharField(
        _("type"), 
        max_length=50, 
        blank=False, 
        null=False)
    user = models.ForeignKey(
        User, 
        null=False, 
        blank=False, 
        on_delete=models.CASCADE)
    is_active = models.BooleanField(
        _("Is Active"), 
        default=True)
    created_at = models.DateTimeField(
        auto_now=True, 
        auto_now_add=False, 
        help_text="When This Object Created")
    
    
    class Meta:
        verbose_name = "API Token"
        ordering = ['-created_at']

    def __str__(self):
        return self.key