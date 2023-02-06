from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.permissions import AllowAny
from django.db.models import Count
from django.http import JsonResponse
from django.http import Http404

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


  def get(self, request,pk=None, *args, **kwargs):
    """
    API End Point to fetch the tasks or a specific task created by the requested user.
    """
    if pk:
      task = self.get_object(pk)

      #returns data only if the task is created by the requested user.
      if request.user.id == task.user.id:
        serializer = ToDoModelSerializer(task)
        return Response(serializer.data)

      #forbidden message for unauthorised user.
      message = {
        "message":"Forbidden"
      }
      return Response(message,status=status.HTTP_403_FORBIDDEN)

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


  def put(self, request, pk, *args, **kwargs):
    """
    API End Point to update a task created by the requested user.
    """
    task = self.get_object(pk)

    #validates if the task belongs to the requested user.
    if request.user.id != task.user.id:
      message = {
        "message":"Forbidden"
      }
      return Response(message,status=status.HTTP_403_FORBIDDEN)

    #updating the task.
    serializer = ToDoModelSerializer(task, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def delete(self, request, pk,*args, **kwargs):
      """
      API End Point to delete a task created by the requested user.
      """
      task = self.get_object(pk)

      #validates if the task belongs to the requested user.
      if request.user.id != task.user.id:
        message = {
          "message":"Forbidden"
        }
        return Response(message,status=status.HTTP_403_FORBIDDEN)

      #deleting the requested task.
      task.delete()
      message = {
        "message":"Task deleted successfully"
      }
      return Response(message,status=status.HTTP_204_NO_CONTENT)


  def get_object(self, pk):
    """
    Function for fetching an single object with the primary key passed.
    """
    try:
      task = toDoList.objects.get(id=pk)
      return task
    except toDoList.DoesNotExist:
      raise Http404


    
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
