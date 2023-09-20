import decimal
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import OrcamentoProdutoForm, OrcamentoMaoDeObraForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from .models import Orcamento, ItemProduto, ItemMaoDeObra
from .forms import OrcamentoUpdateForm
from apps.core.ultils import GeradorKeys
import numpy
from .calculos_orcamentos import ValoresOrcamento
from ..pix.models import QrPix
from pypix import Pix
from decimal import Decimal
from apps.core.gerador_pix import novo_qrpix_orcamento
class GerarOrcamentoView(LoginRequiredMixin, DetailView):
    model = Orcamento
    template_name = 'orcamentos/orcamento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orcamento = self.get_object().id
        valores = ValoresOrcamento(orcamento_id=orcamento)
        context = super().get_context_data(**kwargs)
        context['total_produtos'] = valores.total_orcamento()['total_produtos']
        context['total_maos_de_obras'] = valores.total_orcamento()['total_mao_de_obra']
        context['total_orcamento'] = valores.total_orcamento()['total_orcamento']
        return context


class ImprimirOrcamento(GerarOrcamentoView):
    template_name = 'orcamentos/orcamento_impressao.html'

    def get_context_data(self, **kwargs):
        context = super(ImprimirOrcamento, self).get_context_data(**kwargs)
        # if QrPix.objects.filter(orcamento_id=self.object.id).exists():
        #     context['qrcode_cliente'] = QrPix.objects.get(orcamento=self.object)
        # else:
        #     import base64
        #     from django.core.files.base import ContentFile
        #     _valor = context['total_orcamento'].split(' ')[1]
        #     valor = float(_valor.replace('.', '').replace(',', '.'))
        #
        #     data = self.create_qrcode(valor)
        #
        #     format, imgstr = data.split(';base64,')
        #
        #     ext = format.split('/')[-1]
        #     data = ContentFile(base64.b64decode(imgstr), name=f'pix_cliente{self.object.id}.' + ext)
        #
        #     QrPix.objects.create(
        #         orcamento=self.object,
        #         total=valor,
        #         qr_code=data
        #     )
        context['qrcode_cliente'] = novo_qrpix_orcamento(instance=self.object, value=context['total_orcamento'])
        return context


    def create_qrcode(self, amount):

        pix = Pix()
        pix.set_name_receiver('Marcio Oliveira de Deus')
        pix.set_city_receiver('aguasdelindoia')
        pix.set_key('04855527440')
        pix.set_identification('123')
        pix.set_zipcode_receiver('13940000')
        pix.set_description('mod64bits')
        pix.set_amount(amount)
        base64qr = pix.save_qrcode('./qrcode.png', color="green", box_size=7,
                                   border=1,
                                   )


        return base64qr


class OrcamentosView(LoginRequiredMixin, ListView):
    model = Orcamento
    paginate_by = 100
    template_name = 'orcamentos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_orcamento'] = True
        context['active_orcamento'] = True
        return context


class NovoOrcamento(LoginRequiredMixin, CreateView):
    form_class = OrcamentoUpdateForm
    template_name = 'orcamentos/orcamento_form.html'

    def form_valid(self, form):
        key_orcamento = GeradorKeys(user_id=self.request.user.id, cliente_id=form.instance.cliente.id)
        form.instance.codigo = key_orcamento.key()
        return super(NovoOrcamento, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_orcamento'] = True
        context['active_orcamento_novo'] = True

        return context


class OrcamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Orcamento
    form_class = OrcamentoUpdateForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orcamento = self.get_object().id
        valores = ValoresOrcamento(orcamento_id=orcamento)
        context['total_produtos'] = valores.total_orcamento()['total_produtos']
        context['total_maos_de_obras'] = valores.total_orcamento()['total_mao_de_obra']
        context['total_orcamento'] = valores.total_orcamento()['total_orcamento']
        context['total_lucro'] = valores.total_orcamento()['total_lucro']
        context['qt_produtos'] = valores.quabtidade_produtos()
        context['qt_mao_de_obra'] = valores.quantidade_mao_de_obra()
        context['menu_open_orcamento'] = True

        return context


class AdcionarProdutoView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'orcamentos/adcionar_item.html'
    form_class = OrcamentoProdutoForm
    success_message = 'Success: Book was created.'

    def form_valid(self, form):
        orcamento = Orcamento.objects.get(id=self.kwargs['pk'])
        qt = form.instance.quantidade
        if ItemProduto.objects.filter(produto_id=form.instance.produto.id, orcamento=orcamento).exists():
            produto = ItemProduto.objects.get(produto_id=form.instance.produto.id, orcamento=orcamento)
            form.instance = produto
            form.instance.quantidade += qt
        form.instance.orcamento = orcamento

        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdcionarProdutoView, self).form_valid(form)


class AdiconarMaoDeObraView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'orcamentos/adcionar_mao_de_obra.html'
    form_class = OrcamentoMaoDeObraForm
    success_message = 'Mão de obra adcionado com sucesso!'

    def form_valid(self, form):
        orcamento = Orcamento.objects.get(id=self.kwargs['pk'])
        qt = form.instance.quantidade
        if ItemMaoDeObra.objects.filter(mao_de_obra_id=form.instance.mao_de_obra.id,
                                        orcamento_id=self.kwargs['pk']).exists():
            mao_obra = ItemMaoDeObra.objects.get(mao_de_obra_id=form.instance.mao_de_obra_id,
                                                 orcamento_id=self.kwargs['pk'])
            form.instance = mao_obra
            form.instance.quantidade += qt
        else:
            form.instance.orcamento = orcamento
            form.instance.id = None

            form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdiconarMaoDeObraView, self).form_valid(form)


class EditarItemProdutoView(BSModalUpdateView):
    model = ItemProduto
    template_name = 'orcamentos/editar_item_produto.html'
    form_class = OrcamentoProdutoForm

    def form_valid(self, form):
        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)
        return super(EditarItemProdutoView, self).form_valid(form)


class ItemProdutoDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = ItemProduto
    template_name = 'orcamentos/delete_item_produto.html'
    success_message = 'Success: Categoria excluída com sucesso.'

    def get_success_url(self):
        orcamento = self.get_object()
        return reverse('orcamento:update_orcamento', kwargs={'pk': orcamento.orcamento.id})


    # TODO Adcionar edição de item mão de obra