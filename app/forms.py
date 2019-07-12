from django import forms
from models import inscricao 


class PedidoForm(forms.ModelForm):
    class Meta:
        model = inscricao
        fields = [
            'cpf',
            'email',
            'endereco',
            'cartao',
            'pagamento'
]