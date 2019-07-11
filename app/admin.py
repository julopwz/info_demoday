from django.contrib import admin
from .models import Lugar
from .models import Loja
from .models import Restaurante
from .models import Servico
# Register your models here.

admin.site.register(Lugar)
admin.site.register(Loja)
admin.site.register(Restaurante)
admin.site.register(Servico)