from django.shortcuts import render
from rest_framework import viewsets

from .serializer import ToDoModelSerializer,UserModelSerializer
from project.models import toDoList
from django.contrib.auth.models import User

# Create your views here.

class ToDoViewSet(viewsets.ModelViewSet):
  queryset = toDoList.objects.all()
  serializer_class = ToDoModelSerializer

class UsersViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserModelSerializer
