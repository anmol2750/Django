from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from django.contrib.auth.models import User
from . import constants

class SignupAPIView(APIView):

    def get(self,request):
        objects = User.objects.all()

        obj_data = []
        for object in objects:
            obj_data.append({
                'username' : object.username,
                'email' : object.email,
                'first_name' : object.first_name,
                'last_name' : object.last_name,
            })

        data = {'objects' : obj_data}

        return Response(data, status = status.HTTP_200_OK)

    def post(self,request):
        try:
            obj =  SignupSerializer(data =  request.data)
            if obj.is_valid():
                obj.save()
                return Response({'Message': constants.SIGNED_UP_MESSAGE},status = status.HTTP_200_OK)
            return Response(obj.errors, status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message': constants.FAILED_MESSAGE.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)

    