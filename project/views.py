from asyncio import tasks
from django.shortcuts import redirect, render
from django.http import HttpResponse
from matplotlib.style import context

from project.forms import ProjectForm
from .models import toDoList

# Create your views here.
def homePage(request):
    template = 'project/index.html'
    return render(request,template)

def addProject(request):
    tasks = ProjectForm()
    context = {}
    template = 'project/toDoEntry.html'
    context['tasks'] = tasks

    if request.method == 'POST':
        tasks = ProjectForm(request.POST)
        if tasks.is_valid():
            tasks.save()
            return redirect('viewtasks')
    return render(request,template,context)

def displayTask(request):
    tasks = toDoList.objects.all()
    template = 'project/view.html'
    context = {}
    context['tasks']=tasks
    return render(request,template,context) 

def deleteTask(request,pk):
       tasks = toDoList.objects.all()
       template = 'project/view.html'
       context = {}
       context['tasks'] = tasks 
       context['delete'] = True
       if request.method == 'POST':
           tasks = toDoList.objects.get(id=pk)
           tasks.delete()
           return redirect('viewtasks')
       return render(request,template,context)

def updateTask(request,pk):
    objects = toDoList.objects.get(id=pk)
    tasks = ProjectForm(instance=objects)
    context = {}
    context ['tasks'] = tasks
    template = 'project/toDoEntry.html'
    if request.method == 'POST':
        tasks = ProjectForm(request.POST,instance=objects)
        if tasks.is_valid:
            tasks.save()
            return redirect('viewtasks')
    return render(request,template,context)

def updateStatus(request,pk):
    objects = toDoList.objects.get(id=pk)
    if objects.status == "Incomplete":
        objects.status = "Completed"
    else:
        objects.status = "Incomplete"

    objects.save()
    return redirect('viewtasks')
       