from django.shortcuts import render, redirect
from app.forms import CadastroForm, LoginForm, BuscaForm, ContatoForm, EmpresaForm
from app.models import Cadastro, Lugar, loja, restaurante, Servico, Contato, empresa

def mostrar_empresa(request):
    empresa = EmpresaForm()
    return render(request, "empresa.html", {'empresa':empresa})

def mostrar_sobrenos(request):
    return render(request,'sobre-nos.html')

def mostrar_loja(request):
    lojas = loja.objects.all()
    return render(request, 'loja.html', {'lojas':lojas})

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_layout(request):
    return render(request,'layout.html')

def mostrar_comofunciona(request):
    return render(request, 'como-funciona.html')


def mostrar_restaurante(request):
    restaurantes = restaurante.objects.all()
    return render(request, 'restaurante.html', {'restaurantes':restaurantes})

def mostrar_servico(request):
    return render(request, 'servico.html')

def mostrar_contato(request):
    formulario = ContatoForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = ContatoForm()
        msg = 'Mensagem enviada com sucesso'

    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'contato.html', contexto)

def mostrar_busca(request):
    form_busca = BuscaForm(request.POST or None)
    medicos = []
    
    if form_busca.is_valid():
        pesquisa = form_busca.cleaned_data['pesquisa']
        sigla = buscar_sigla_especialidade(pesquisa)
        medicos = Medico.objects.filter(especialidade=sigla)
        
    return render(request, 'busca.html', {'form': form_busca, 'medicos': medicos})

def mostrar_cadastro(request):
    formulario_cadastro = CadastroForm(request.POST or None)
    msg = ' '

    if formulario_cadastro.is_valid():
        formulario_cadastro.save()
        formulario_cadastro = CadastroForm()
        msg = 'Cadastro criado com sucesso'
        return redirect('/busca')

    contexto = {
        'form' : formulario_cadastro,
        'msg' : msg
    }

    return render(request, 'cadastro.html', contexto)

def mostrar_login(request): 
    formulario_login = LoginForm(request.POST or None)
    msg = ' '
    if formulario_login.is_valid():
        username = formulario_login.cleaned_data['username']
        password = formulario_login.cleaned_data['password']
        user = Cadastro.objects.filter(username=username).first()
        
        if not user or user.password != password:
            msg = ''
        else:
            return redirect('/busca')

    return render(request, 'login.html', {'form': formulario_login, 'msg': msg})