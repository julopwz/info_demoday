from django.contrib import admin
from app.models import Cadastro, Contato, Lugar, Restaurante, Loja, Servico
# Register your models here.

admin.site.register(Cadastro)
admin.site.register(Lugar)
admin.site.register(Loja)
admin.site.register(Restaurante)
admin.site.register(Servico)
admin.site.register(Contato) 