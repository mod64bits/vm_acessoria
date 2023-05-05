from django.forms import ModelForm, Textarea
from .models import MaoDeObra, TipoDeMaoDeObra
from bootstrap_modal_forms.forms import BSModalModelForm


class MaoDeObraForm(BSModalModelForm):
    class Meta:
        model = MaoDeObra
        fields = '__all__'
        widgets = {
            "descricao": Textarea(attrs={"cols": 20, "rows": 5}),
        }



class TipoDeMaoDeObraForm(BSModalModelForm):
    class Meta:
        model = TipoDeMaoDeObra
        fields = '__all__'

