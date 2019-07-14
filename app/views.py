from django.shortcuts import render
from app.forms import ContatoForm, CadastroForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_layout(request):
    return render(request,'layout.html')

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

def mostrar_sobrenos(request):
    return render(request,'sobre-nos.html')

def mostrar_comofunciona(request):
    return render(request, 'como-funciona.html')

def mostrar_pagina4(request):
    return render(request, 'pagina4.html')

def mostrar_pagina2(request):
    return render(request, 'pagina2.html')

def mostrar_pagina3(request):
    return render(request, 'pagina3.html')

def mostrar_cadastro(request):
    formulario_cadastro = CadastroForm(request.POST or None)
    msg = ' '

    if formulario_cadastro.is_valid():
        formulario_cadastro.save()
        formulario_cadastro = CadastroForm()
        msg = 'Cadastro criado com sucesso'

    contexto = {
        'form' : formulario_cadastro,
        'msg' : msg
    }

    return render(request, 'cadastro.html', contexto)
    
def mostrar_login(request): 
    formulario_login = LoginForm(request.POST or None)
    msg = ''
    if formulario_login.is_valid():
        username = formulario_login.cleaned_data['username']
        password = formulario_login.cleaned_data['password']
        user = Cadastro.objects.filter(username=username).first()
        
        if not user or user.password != password:
            msg = ''
        else:
            return redirect('/busca')

    return render(request, 'login.html', {'form': formulario_login, 'msg': msg})

def logout(request):
    return redirect('login/')
