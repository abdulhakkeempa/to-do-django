from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.permissions import AllowAny
from django.db.models import Count
from django.http import JsonResponse

from .serializer import ToDoModelSerializer,UserModelSerializer
from project.models import toDoList
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.

class ToDoViewSet(views.APIView):
  queryset = toDoList.objects.all()
  serializer_class = ToDoModelSerializer
  permission_classes = [IsAuthenticated]
  lookup_field = 'id'

  def get(self, request, *args, **kwargs):
    """
    API End Point to fetch the tasks created by the requested user.
    """
    queryset = toDoList.objects.filter(user=self.request.user)
    data = ToDoModelSerializer(queryset,many=True)
    return Response(data.data)

  def post(self, request, *args, **kwargs):
    """
    API End Point to create a task for a requested user.
    """
    serializer = ToDoModelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    task = serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

  def get_object(self, pk):
    """
    API Endpoint for fetching an single object with the primary key passed.
    """
    try:
      task = toDoList.objects.get(id=pk)
      serializer = ToDoModelSerializer(task)
    except toDoList.DoesNotExist:
      message = {
        "message":"Data not found"
      }
      raise Response(message,status=status.HTTP_404_NOT_FOUND)
    
    #self.user is logged user not jwt user
    print(self.user.id)
    print(task.user.id)

    if task.user.id == self.user.id:
      return JsonResponse(serializer.data,status=status.HTTP_200_OK)
    else:
      message = {
        "message":"Forbidden"
      }
      return JsonResponse(message,status=status.HTTP_403_FORBIDDEN)


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
