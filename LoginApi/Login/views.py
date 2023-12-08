from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import constants

# Create your views here.
class LoginAPIView(APIView):

    def post(self,request):        
        username = request.data.get('username',None)
        password =  request.data.get('password',None)

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return Response({'Message': constants.LOGGED_MESSAGE},status = status.HTTP_200_OK)
        else:
            return Response({'Message': constants.INVALID_MESSAGE},status = status.HTTP_401_UNAUTHORIZED)
