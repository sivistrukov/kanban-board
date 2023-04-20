from rest_framework import viewsets
from rest_framework import permissions

from board.api.serializers import TaskSerializer
from board.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
