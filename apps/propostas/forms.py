from django import forms
from django.forms import fields, models, formsets, widgets, CheckboxInput
from .models import Orcamento, Proposta


class OrcamentoForm(models.ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'


class PropostaForm(models.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Proposta
        fields = ['orcamento']

    class Media:
        js = ('js/jquery.autocomplete.min.js', 'js/autocomplete-init.js',)
        css = {
            'all': ('css/jquery.autocomplete.css',),
        }


class PropostaDetalheForm(PropostaForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
        self.fields['validade'].widget.attrs['readonly'] = True
        # self.fields['orcamento'].widget.attrs['readonly'] = True
    class Meta:
        model = Proposta
        exclude = ['orcamento', 'qr_code']
        widgets = {
            'finalizado': CheckboxInput(attrs={'weight': '15px'}),
        }

    # def save(self, commit=True):
    #     obj = super(PropostaDetalheForm, self).save(commit=False)
    #     print()

class SelectPropostaForm(forms.Form):
    orcamento = forms.ChoiceField(choices=[
    (choice.pk, choice) for choice in Orcamento.objects.all()])


