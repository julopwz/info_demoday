from django import forms
from app.models import Contato, Cadastro
from django.conf.global_settings import DATETIME_INPUT_FORMATS

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'email',
            'nascimento',
            'telefone',
            'username',
            'password'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label= 'Senha', widget=forms.PasswordInput())


class BuscaForm(forms.Form):
    pesquisa = forms.CharField(label='Pesquisa')

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
           'nome',
           'email',
           'telefone',
           'assunto',
           'mensagem',
        ]