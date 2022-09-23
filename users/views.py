from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import generics

# Create your views here.

#class based view to get user details using token authentication
class UserDetail(APIView):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(AllowAny,)

    def get(user,request,*args,**kwargs):
        user=User.objects.get(id = request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#class based view for signup 
class SignupUser(generics.CreateAPIView):
    permission_classes=(AllowAny,)
    serializer_class=RegisterSerializer