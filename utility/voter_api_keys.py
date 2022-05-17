import jwt
from datetime import timedelta, datetime

from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import exceptions

from voter.models import APItoken, VoterUser


class VoterTokens:

    @staticmethod
    def _generate_token(payload: dict, key: str, token_type: str,
                        algorthm: str, user: User):
        """
        base function to generate jwt token
        """
        token = jwt.encode(payload, key, algorithm=algorthm)
        APItoken.objects.create(key=token, type=token_type,
                                user=user, is_active=True)
        return token

    @staticmethod
    def generate_verify_token(voter, expire=10, token_type="Bearer", name="veify"):
        key = settings.API_KEY
        algorthm = settings.API_ALGORTHM
        payload = {
            "name": name,
            "id": voter.id,
            "is_expire": voter.is_expire,
            "exp": timezone.now() + + timedelta(minutes=10),
            "time": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }

        return VoterTokens._generate_token(payload=payload, key=key, token_type=token_type,
                                           algorthm=algorthm, user=voter.user)

    @staticmethod
    def from_verify_token(token, type):
        if not APItoken.objects.filter(key=token, type=type, is_active=True).last():
            raise exceptions.AuthenticationFailed('Invalid Token')
        key = settings.API_KEY
        algorthm = settings.API_ALGORTHM
        try:
            data = jwt.decode(token, key, algorithms=algorthm)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Expired OTP')
        return VoterUser.objects.filter(id=data.get('id')).last()
