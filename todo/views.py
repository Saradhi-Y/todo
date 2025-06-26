from django.shortcuts import render,HttpResponse,redirect
from .models import Task


def addTask(request):
    task =request.POST['task']
    Task.objects.create(task=task) #first task is task from model Task and second task is above variable
    return redirect('home')
