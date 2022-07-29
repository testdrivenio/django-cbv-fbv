from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    context_object_name = 'task'
    fields = ('name', 'description', 'is_done')
    template_name = 'todo/task_create.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    fields = ('name', 'description', 'is_done')
    template_name = 'todo/task_update.html'


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/'
