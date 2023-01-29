from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


from .serializer import ToDoModelSerializer,UserModelSerializer
from project.models import toDoList
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.

class ToDoViewSet(viewsets.ModelViewSet):
  queryset = toDoList.objects.all()
  serializer_class = ToDoModelSerializer

class UsersViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserModelSerializer
  permission_classes = [IsAuthenticated]


class UserCreateAPI(generics.GenericAPIView):
  serializer_class = UserModelSerializer
  permission_classes = [AllowAny]

  def post(self, request, *args, **kwargs):
    """
    Post: endpoint to create a new user for register route.
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)