from django.utils import timezone
import logging

from django.conf import settings

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from voter.models import VoterUser
from voter.serializers import VoterSerializer

from utility.error_code import ErrorCodes
from utility.voter_api_keys import VoterTokens
from utility.otp_email import OTPEmail

logger = logging.getLogger(__name__)


class RegisterView(generics.GenericAPIView):
    queryset = VoterUser.objects.all()
    serializer_class = VoterSerializer
    permission_classes = (AllowAny, )

    def get_verify_token(self, voter: VoterUser, otp: str):
        """
            - Update voter OTP data
            - Get token used in verify endpoint 
        """
        voter.otp_sent = True
        voter.last_otp = otp
        voter.otp_sent_date = timezone.now()
        voter.save()

        # Call VoterToken
        return VoterTokens.generate_verify_token(voter)

    def post(self, request):
        """
            Register View
        """
        data = self.request.data
        logger.debug('[REGISTER][POST] register input IS: {}'.format(data))

        serializer = VoterSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors,
                                  "error_code": ErrorCodes.serializer_error.value},
                            status=status.HTTP_400_BAD_REQUEST)

        voter = serializer.save()

        otp = OTPEmail.generate_random_otp()
        otp_sent = OTPEmail.send_otp_email(username=serializer.validated_data['username'],
                                           subject="Verify your registeration",
                                           from_email=settings.OPERATION_TEAM,
                                           to_email=serializer.validated_data['email'],
                                           otp=otp
                                           )
        if not otp_sent:
            return Response(data={"message": "Failed to sent OTP, Please try again later",
                                  "error_code": ErrorCodes.opt_error.value},
                            status=status.HTTP_400_BAD_REQUEST)

        logger.debug('[REGISTER][OTP] OTP sent successfully')

        verify_token = self.get_verify_token(voter=voter, otp=otp)

        logger.debug('[REGISTER][VERIFY TOKEN] successfully created')

        return Response(data={
            "message": "Register Successfully",
            "verify_token": verify_token}, status=status.HTTP_201_CREATED)
