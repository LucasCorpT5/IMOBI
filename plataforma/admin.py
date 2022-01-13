from django.contrib import admin
from .models import Imagem, Cidade, DiasVisita, Horario, Imovei, Visitas

# Register your models here.
admin.site.register(DiasVisita)
admin.site.register(Cidade)
admin.site.register(Imagem)
admin.site.register(Horario)
admin.site.register(Imovei)
admin.site.register(Visitas)