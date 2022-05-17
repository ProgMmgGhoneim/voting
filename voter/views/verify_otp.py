from django.utils import timezone
import logging

from django.conf import settings

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


from utility.authontication import verifyAuthentication
from utility.error_code import ErrorCodes

logger = logging.getLogger(__name__)


class VerifyView(generics.GenericAPIView):
    authentication_classes = [verifyAuthentication, ]

    def post(self, request):
        otp = request.data.get('otp')
        voter = request.user
        
        if not otp:
            return Response(data={
                "message": "OTP is required",
                "error_code": ErrorCodes.serializer_error.value
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if voter.last_otp != otp:
            return Response(data={
                "message": "Inavlid OTP",
                "error_code": ErrorCodes.serializer_error.value
            }, status=status.HTTP_400_BAD_REQUEST)  
        
        voter.is_verified = True
        voter.save()
          
        return Response(data={
                "message": "your account is verified now",
            }, status=status.HTTP_200_OK) 