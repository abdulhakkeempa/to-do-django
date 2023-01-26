from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import toDoList


class ToDoModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = toDoList
    fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['password']