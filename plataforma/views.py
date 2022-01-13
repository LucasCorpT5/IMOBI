from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  .models import Imovei, Cidade

# Create your views here.
@login_required(login_url="/auth/login")
def home(request):
    preco_minimo = request.GET.get("preco_minimo")
    preco_maximo = request.GET.get("preco_maximo")
    cidade = request.GET.get("cidade")
    tipo = request.GET.getlist("tipo")

    if preco_minimo or preco_maximo or cidade or tipo:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 9999999999999999

    print(f'PM {preco_minimo} PMAX {preco_maximo} cidade {cidade} tipo {tipo}')
    imoveis = Imovei.objects.all()
    cidades = Cidade.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})