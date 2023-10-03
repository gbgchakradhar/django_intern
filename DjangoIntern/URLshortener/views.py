from django.shortcuts import render
from .models import task

def task_list(request):
    tasks = task.objects.all() 
    context = {'tasks': tasks}
    return render(request, 'task.html', context)
