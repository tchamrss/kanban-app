from django.contrib import admin

from tasks.models import Tasks, tasks_board

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    fields = ('task_board','title','description', 'author', 'due_date') 
    list_display = ('task_board','title','description', 'author', 'due_date', 'priority')
    search_fields = ('title',)

admin.site.register(Tasks,TasksAdmin)
admin.site.register(tasks_board)
