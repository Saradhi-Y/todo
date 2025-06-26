from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed=False) #here we are fetching tasks from model to view
    context={
        'tasks':tasks
        }
    return render(request,'home.html',context)