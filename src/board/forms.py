from django import forms

from board.models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'column')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded px-2 py-1'
            }),
            'column': forms.Select(attrs={
                'class': 'border bg-white rounded px-2 py-1'
            })
        }
