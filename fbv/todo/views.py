from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, ConfirmForm
from .models import Task


def task_list_view(request):
    return render(request, 'todo/task_list.html', {
        'tasks': Task.objects.all(),
    })


def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task-detail', pk=task.pk)

    return render(request, 'todo/task_create.html', {
        'form': TaskForm(),
    })


def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render(request, 'todo/task_detail.html', {
        'task': task,
    })


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=task.pk)

    return render(request, 'todo/task_update.html', {
        'task': task,
        'form': TaskForm(instance=task),
    })


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = ConfirmForm(data=request.POST)
        if form.is_valid():
            task.delete()
            return redirect('task-list')

    return render(request, 'todo/task_confirm_delete.html', {
        'task': task,
        'form': ConfirmForm(),
    })
