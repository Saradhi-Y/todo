from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at') #these are shown in admin panel
    search_fields=('task',)  #it adds search field in admin panel

admin.site.register(Task,TaskAdmin)
