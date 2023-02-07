from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Sobre


class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sobre'] = Sobre.objects.first()
        return context
