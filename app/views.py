from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_layout(request):
    return render(request,'layout.html')

def mostrar_pagina1(request):
    return render(request,'pagina1.html')

def mostrar_pagina2(request):
    return render(request,'pagina2.html')

def mostrar_pagina3(request):
    return render(request,'pagina3.html')
