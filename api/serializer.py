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
    fields = ('id','username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    """To create a new auth.user model"""
    user = User.objects.create_user(**validated_data)
    return user


