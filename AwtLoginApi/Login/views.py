from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from . import constant
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPI(APIView):

    def post(self, request):
        try:
            data = request.data 
            serializer = LoginSerializer(data = data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                user = authenticate(username = username, password = password)
                if user is None:
                    return Response({'Message' : 'Invalid Username or password', 'status' : 'HTTP_400_BAD_REQUEST', 'data' : {}})
                
                refresh = RefreshToken.for_user(user)
                return Response({'refresh' : str(refresh), 'access' : str(refresh.access_token)})
        except Exception as e:
            return Response({'Message': constant.FAILED_MESSAGE.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)

    # def get(self,request):
    #     objects = User.objects.all()

    #     objects_data = []
    #     for object in objects:
    #         objects_data.append({
    #             'username' : object.username,
    #             'first_name' : object.first_name,
    #             'last_name' : object.last_name,
    #         })

    #     data = {'objects' : objects_data}
    #     return Response(data, status =  status.HTTP_200_OK)      