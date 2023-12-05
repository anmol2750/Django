from rest_framework import serializers
from  .models import user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
 
    class Meta:
        model = user
        fields = ('__all__')