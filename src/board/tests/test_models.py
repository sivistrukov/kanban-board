import datetime

from django.test import TestCase

from board.models import Column, Task


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.column = Column.objects.create(title='Column', order=1)

    def test_task_name_max_length_not_exceed(self):
        # will not pass if used SQLite
        task = Task.objects.create(name='X' * 300, column=self.column)
        max_length_name = task._meta.get_field('name').max_length
        length_name = len(task.name)
        self.assertEqual(length_name, max_length_name)

    def test_task_auto_fill_fields(self):
        new_task = Task.objects.create(name='New task', column=self.column)
        self.assertNotEquals(new_task.created, '')
        self.assertEqual(type(new_task.created), datetime.datetime)
        self.assertNotEquals(new_task.updated, '')
        self.assertEqual(type(new_task.updated), datetime.datetime)



