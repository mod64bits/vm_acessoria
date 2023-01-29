from django.forms import ModelForm
from .models import Cliente, TelefoneContato
from bootstrap_modal_forms.forms import BSModalModelForm


class ClienteForm(BSModalModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class TelefoneForm(ModelForm):
    class Meta:
        model = TelefoneContato
        fields = '__all__'
