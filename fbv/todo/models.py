from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=512, blank=True, null=True)
    is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/{self.pk}/'

    def __str__(self):
        return f'Task #{self.id}'
