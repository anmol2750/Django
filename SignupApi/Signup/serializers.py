from rest_framework import serializers
from django.contrib.auth.models import User
from . import constants

class SignupSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(max_length = 20)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length = 30)
    last_name =  serializers.CharField(max_length = 30)
    password =  serializers.CharField(max_length = 10)
    confirm_password = serializers.CharField(max_length = 10)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirm_password')

    def create(self,validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self,value):

        if value.get('password') != value.get('confirm_password'):
            raise serializers.ValidationError(constants.PASSWORD_MATCH_ERROR)
        return value