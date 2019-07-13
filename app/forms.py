from django import forms
from app.models import Cadastro


class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cadastro
        fields = [
            'usuario',
            'senha',
            'cpf',
            'email',
            'celular'
        ]