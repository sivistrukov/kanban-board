from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from board.api.serializers import TaskSerializer
from board.models import Column, Task

User = get_user_model()


class TasksAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='username', email='useremail@mail.com', password='password'
        )
        self.columns = [
            Column.objects.create(title='Await', order='1'),
            Column.objects.create(title='Done', order='2'),
        ]
        self.tasks = [
            Task.objects.create(name='Task 1', column_id=1),
            Task.objects.create(name='Task 2', column_id=2),
        ]
        self.base_url = '/api/board/tasks/'

    def test_get_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.base_url)
        serialized_data = TaskSerializer(self.tasks, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serialized_data, response.data)

    def test_get_list_deny_anonymous(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.base_url + '1/')
        serialized_data = TaskSerializer(self.tasks[0]).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serialized_data, response.data)

    def test_get_detail_deny_anonymous(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
