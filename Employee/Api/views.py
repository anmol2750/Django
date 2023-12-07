from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeView(APIView):
    def post(self, request):
        username = request.data.get(EmployeeSerializer.username,None)
        password = request.data.get(EmployeeSerializer.password,None)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'Message':'Logged In'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message':'Invalid username and password combination'}, status=status.HTTP_400_BAD_REQUEST)