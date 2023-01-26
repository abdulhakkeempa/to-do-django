from django.shortcuts import render
from rest_framework import viewsets

from .serializer import ToDoModelSerializer
from project.models import toDoList

# Create your views here.

class ToDoViewSet(viewsets.ModelViewSet):
  queryset = toDoList.objects.all()
  serializer_class = ToDoModelSerializer