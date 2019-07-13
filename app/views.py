from django.shortcuts import render
from app.forms import ContatoForm, CadastroForm


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

def mostrar_cadastro(request):
    formulario = CadastroForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm()
        msg = 'Cadastro com sucesso'

    contexto = {
        'form' : formulario,
        'msg' : msg
    }

    return render(request, 'cadastro.html', contexto)

def mostrar_pagina2(request):
    return render(request,'pagina2.html')

def mostrar_pagina3(request):
    return render(request,'pagina3.html')

def mostrar_pagina4(request):
    return render(request, 'pagina4.html')