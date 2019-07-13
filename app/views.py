from django.shortcuts import render

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_layout(request):
    return render(request,'layout.html')

def mostrar_contato(request):
    return render(request, 'contato.html')

def mostrar_sobrenos(request):
    return render(request,'sobre-nos.html')

def mostrar_comofunciona(request):
    return render(request, 'como-funciona.html')

def mostrar_cadastro(request):
    return render(request, 'cadastro.html')

def mostrar_pagina2(request):
    return render(request,'pagina2.html')

def mostrar_pagina3(request):
    return render(request,'pagina3.html')

def mostrar_pagina4(request):
    return render(request, 'pagina4.html')