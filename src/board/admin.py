from django.contrib import admin

from .models import Column, Task


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'column', 'created', 'updated')
    list_filter = ('column',)
    fields = ('name', 'column')
