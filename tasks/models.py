from django.db import models
from datetime import date
from django.conf import settings


class tasks_board(models.Model):
    created_at = models.DateField(default=date.today)


class Tasks(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    created_at =  models.DateField(default=date.today)
    priority = models.CharField(max_length=10)
    due_date = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_task_set')
    task_board = models.ForeignKey(tasks_board, on_delete=models.CASCADE, related_name='board_task_set', default=None, blank=True, null=True)
