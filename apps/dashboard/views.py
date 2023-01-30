from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_dashboard'] = True
        return context
