from django.db import models


class Column(models.Model):
    title = models.CharField(max_length=254)
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'

    def __str__(self):
        return str(self.title)


class Task(models.Model):
    name = models.CharField(max_length=254)
    column = models.ForeignKey(to=Column, related_name='tasks',
                               on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return str(self.name)
