from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from .models import Column
from .forms import NewTaskForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['columns'] = Column.objects.all().order_by('order')
        context['new_task_form'] = NewTaskForm
        return context
