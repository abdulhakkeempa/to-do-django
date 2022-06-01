from asyncio import tasks
from dataclasses import field
from django import forms

from matplotlib import widgets
from .models import toDoList
from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
        model = toDoList
        fields = '__all__'
        exclude = ['status']
