from django import forms
from django.forms import ModelForm
from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class ConfirmForm(forms.Form):
    confirm = forms.BooleanField(label='Confirm')
