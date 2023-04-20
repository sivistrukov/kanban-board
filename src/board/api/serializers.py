from rest_framework import serializers

from board.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'column', 'created')
        read_only_fields = ('id', 'created',)
