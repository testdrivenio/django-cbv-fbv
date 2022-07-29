from django.urls import path
from .views import task_list_view, task_detail_view, task_create_view, task_update_view, task_delete_view

urlpatterns = [
    path('', task_list_view, name='task-list'),
    path('create/', task_create_view, name='task-create'),
    path('<int:pk>/', task_detail_view, name='task-detail'),
    path('update/<int:pk>/', task_update_view, name='task-update'),
    path('delete/<int:pk>/', task_delete_view, name='task-delete'),
]
