from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.permissions import AllowAny
from django.db.models import Count


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

class ToDoViewSet(generics.GenericAPIView):
  queryset = toDoList.objects.all()
  serializer_class = ToDoModelSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    """
    API End Point to fetch the tasks created by the requested user.
    """
    queryset = toDoList.objects.filter(user=self.request.user)
    data = self.get_serializer(queryset,many=True)
    return Response(data.data)

  def post(self, request, *args, **kwargs):
    """
    API End Point to create a task for a requested user.
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    task = serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

  def get_object(self, pk):
    try:
        return toDoList.objects.get(pk=pk)
    except toDoList.DoesNotExist:
        raise status.HTTP_201_CREATED


class UsersViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserModelSerializer
  permission_classes = [IsAdminUser]


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
