import jwt
from datetime import timedelta
from django.utils import timezone

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import exceptions

from .profile import UserProfile
from .api_token import APItoken


class VoterManager(models.Manager):
    def _create_user(self, email, password, username):
        user, created = User.objects.get_or_create(username=username, email=email)
        if not created:
            return user
        user.set_password(password)
        user.save()
        return user

    def create_voter(self, email, username, password=None,):
        user = self._create_user(email, password, username)
        voter, _ = VoterUser.objects.get_or_create(user=user)
        return voter


class VoterUser(UserProfile):
    is_verified = models.BooleanField(
        _("Is Verified"),
        blank=False,
        default=False)
    otp_sent = models.BooleanField(
        _("Is OTP Sent?"),
        blank=False,
        default=False)
    last_otp = models.CharField(
        _("Last OTP"),
        max_length=100,
        blank=True,
        null=True)
    otp_sent_date = models.DateTimeField(
        _("When OTP expire?"),
        blank=True,
        null=True)

    objects = models.Manager()
    voter = VoterManager()

    class Meta:
        verbose_name = _("Voter")
        verbose_name_plural = _("Voters")

    def __str__(self):
        return f"{self.user}"

    @property
    def is_expire(self):
        import ipdb; ipdb.set_trace()
        if timezone.now() > self.otp_sent_date + timedelta(minutes=10):
            return False
        return True