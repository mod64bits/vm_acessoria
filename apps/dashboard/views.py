from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .dashboard_filters import OrcamentosFilter
from apps.orcamentos.models import Orcamento



class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def total_aprovados(self):
        return Orcamento.objects.filter(status=2).count()

    def total_cancelados(self):
        return Orcamento.objects.filter(status=3).count()

    def total_analise(self):
        return Orcamento.objects.filter(status=1).count()



    def grafico_meses(self):
        dados = []

        qs = Orcamento.objects.all()

        for item in qs:
            if item.created.strftime("%B") in dados:
                continue
            else:
                print(item.created.strftime("%B"))
                dados.append(item.created.strftime("%B"))

        return dados

    def grafico_valores(self):
        valores = []

        MESES = {
            "January": 1,
            "janeiro": 1,
            "February": 2,
            "fevereiro": 2,
            "March": 3,
            "março": 3,
            "April": 4,
            "abril": 4,
            "May": 5,
            "Maio": 5,
            "June": 6,
            "Junho": 6,
            "July": 7,
            "Julho": 7,
            "August": 8,
            "agosto": 8,
            "Setembro": 9,
            "September": 9,
            "October": 10,
            "outubro": 10,
            "November": 11,
            "novembro": 11,
            "December": 12,
            "dezembro": 12

        }

        for item in self.grafico_meses():
            m = Orcamento.objects.filter(created__month=MESES[item]).count()
            valores.append(m)
        return valores

    def get_context_data(self, **kwargs):
        queryset = Orcamento.objects.all()
        filter = OrcamentosFilter(self.request.GET, queryset)
        context = super().get_context_data(**kwargs)
        context['active_dashboard'] = True
        context['filter_form'] = filter
        context['grafico_legenda'] = self.grafico_meses()
        context['grafico_valores'] = self.grafico_valores()
        context['total_aprovados'] = self.total_aprovados()
        context['total_orcamentos'] = Orcamento.objects.all().count()
        context['total_analise'] = self.total_analise()
        context['total_cancelados'] = self.total_cancelados()
        return context

    # TODO: voltar nesse tema quando tiver dados suficiente
