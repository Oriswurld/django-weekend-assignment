from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task-list.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'confirm-delete.html', {'task': task})

