from email.policy import default
from django.db import transaction

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

from voter.models import VoterUser


class VoterSerializer(serializers.Serializer):
   
    username = serializers.CharField(
        max_length=120, allow_blank=False, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, required=True, write_only=True)
    
    def validate(self, attrs):
        voter = VoterUser.objects.filter(user__username=attrs['username'],
                                         user__email=attrs['email'],
                                         is_verified=True)
        if voter:
            raise serializers.ValidationError("Voter Already exists")
        return attrs
    

    @transaction.atomic
    def create(self, validated_data):
        voter = VoterUser.voter.create_voter(
            username=validated_data.get('username'), 
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return voter
    
