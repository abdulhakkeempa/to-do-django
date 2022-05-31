from dataclasses import field
from .models import toDoList
from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
        model = toDoList
        fields = '__all__'
        exclude = ['status']
