from django.shortcuts import render
from django.http import HttpResponse

from project.forms import ProjectForm
from .models import toDoList

# Create your views here.
def homePage(request):
    template = 'project/index.html'
    return render(request,template)

def addProject(request):
    form = ProjectForm()
    context = {}
    template = 'project/toDoEntry.html'
    context['toDoList'] = form
    print("Routed",context)
    return render(request,template,context)

def displayTask(request):
    tasks = toDoList.objects.all()
    template = 'project/view.html'
    context = {}
    context['tasks']=tasks
    return render(request,template,context)    