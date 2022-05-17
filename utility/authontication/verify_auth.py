from rest_framework import authentication, exceptions

from voter.models import VoterUser
from utility.voter_api_keys import VoterTokens


class verifyAuthentication(authentication.BaseAuthentication):

    def get_from_header(self, request):
        return request.META.get("HTTP_AUTHORIZATION")

    def authenticate(self, request):
        get_token = self.get_from_header(request)
        if not get_token:
            raise exceptions.AuthenticationFailed('Authontication Failed!')
        type, token = get_token.split(' ')

        if not get_token:
            raise exceptions.AuthenticationFailed('Authontication Failed')
        try:
            voter = VoterTokens.from_verify_token(token, type)
        except VoterUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Voter')
        return (voter, token)

    def authenticate_header(self, request):
        return 'Bearer'
