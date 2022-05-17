from django.utils import timezone
import logging

from django.conf import settings

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication


from voter.models import VoterUser
from voter.serializers import VoterSerializer

from utility.error_code import ErrorCodes
from utility.voter_api_keys import VoterTokens
from utility.otp_email import OTPEmail

logger = logging.getLogger(__name__)


class RegisterView(generics.GenericAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (AllowAny, )
    
    def post(self, request):
        pass    
    
    