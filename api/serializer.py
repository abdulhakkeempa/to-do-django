from rest_framework import serializers

from project.models import toDoList


class ToDoModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = toDoList
    fields = '__all__'