from django.contrib import admin
from .models import Lugar
from .models import Loja
from .models import Restaurante
from .models import Servico
from .models import Cadastro

admin.site.register(Lugar)
admin.site.register(Loja)
admin.site.register(Restaurante)
admin.site.register(Servico)
admin.site.register(Cadastro) 