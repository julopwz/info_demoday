from django import forms
from app.models import Contato
from app.models import Cadastro
from django.contrib.auth.models import User


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


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
           'nome',
           'email',
           'nascimento',
           'telefone',
           'username',
           'password',
        ]

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuario'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}))
    celular = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Digite seu número'}))
    cpf = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Digite seu CPF'}))
  
    class Meta:
        model = Cadastro
        fields = ['usuario','senha','cpf','email','celular']
        error_messages = {
            'senha':{
                'required':'Este campo é obrigatório'
            },
            'usuario':{
                'required':'Este campo é obrigatório'
            },
            'email':{
                'required':'Escreva um email válido'
            },
            'celular':{
                'required':'Este campo é obrigatório'
            },
            'cpf':{
                'required':'Este campo é obrigatório'
            },
        }

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

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuario'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}))
    celular = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Digite seu número'}))
    cpf = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Digite seu CPF'}))
    
    class Meta:
        model = Cadastro
        fields = ['usuario','senha','cpf','email','celular']
        error_messages = {
           'senha':{
               'required':'Este campo é obrigatório'
            },
           'usuario':{
               'required':'Este campo é obrigatório'
            },
           'email':{
               'required':'Escreva um email válido'
            },
           'celular':{
               'required':'Este campo é obrigatório'
            },
           'cpf':{
               'required':'Este campo é obrigatório'
            },
        }
       # def save(self):
       #  try:
       #     cpf = CelularUsuario(
       #         celular=self.cleaned_data['celular']
       #     ).save()

       #     usuario = Usuario(
       #         login=self.cleaned_data['login'],
       #         senha=make_password(self.cleaned_data['senha']),
       #     ).save()

       #     return True, usuario.id

       #  except:
       #     transaction.rollback()
       #     return False, "Erro ao salvar cliente."


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label= 'Senha', widget=forms.PasswordInput())


