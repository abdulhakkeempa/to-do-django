from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import toDoList


class ToDoModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = toDoList
    fields = '__all__'
    extra_kwargs = {'user': {'read_only': True}}

  def create(self,validated_data):
    """To create a new todo object"""
    user = None
    request = self.context.get("request")
    print(request.user)
    if request and hasattr(request, "user"):
        user = request.user

    task = toDoList.objects.create(user=user,**validated_data)
    return task

class UserModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    """To create a new auth.user model"""
    user = User.objects.create_user(**validated_data)
    return user


